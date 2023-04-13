from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView
from django.db.models import Sum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib import messages
from datetime import datetime
from .models import Task, DailyEnergy
from .forms import DailyEnergyForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()  # accesses the method of the parent
        # gets only the tasks in the database created by the current user
        queryset = queryset.filter(user=self.request.user)
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'energy', 'completed']
    success_url = reverse_lazy('task-list')
    template_name = 'task_create.html'

    def form_valid(self, form):  # marks the created task with the  username
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'energy', 'completed']
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task-list')

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')


class TaskDeleteConfirmView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'task_confirm_delete.html'


class TaskCompleteView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('home')


class TaskSelectView(View):
    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.selected = request.POST.get('selected') == 'on'
        task.save()
        return redirect('task-list')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            selected_tasks = Task.objects.filter(
                selected=True, user=self.request.user)
            total_spoons = selected_tasks.aggregate(total_spoons=Sum('energy'))\
                .get('total_spoons') or 0

            context['selected_tasks'] = selected_tasks
            context['total_spoons'] = total_spoons

        # Clear selected tasks each night
        now = timezone.now()
        last_cleared_date = self.request.session.get('last_cleared_date')
        if last_cleared_date is None:
            # if last_cleared_date is not set in the session, set to today
            last_cleared_date = now.date()
        else:
            last_cleared_date = datetime.strptime(
                last_cleared_date, '%Y-%m-%d').date()

        if last_cleared_date < now.date():
            # gets the tasks that were selected by the user
            selected_tasks = Task.objects.filter(
                selected=True, user=self.request.user)
            # sets them to unselected (which removes them from today's tasks)
            selected_tasks.update(selected=False)
            # sets the 'last cleared date' to the current date
            self.request.session['last_cleared_date'] = now.date().isoformat()

        # get latest daily energy object
        if self.request.user.is_authenticated:
            try:
                last_daily_energy = DailyEnergy.objects.filter(
                    user=self.request.user).latest('created_at')
            except DailyEnergy.DoesNotExist:
                last_daily_energy = None
        else:
            pass

        # check if last daily energy object was created on a previous date
        if self.request.user.is_authenticated:
            now = timezone.now()
            if last_daily_energy is None or\
                    last_daily_energy.created_at.date() < now.date():
                # create new daily energy object for today (resets DailyEnergy)
                daily_energy = DailyEnergy.objects.create(
                    user=self.request.user, created_at=now, user_energy=0)
            else:
                daily_energy = last_daily_energy
            context['daily_energy'] = daily_energy
        else:
            pass

        if self.request.user.is_authenticated:
            # calculate surplus/deficit of energy
            energy_diff = daily_energy.user_energy - total_spoons
            context['energy_diff'] = energy_diff
        else:
            pass

        return context


class ClearTodaysTasks(View):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        Task.objects.filter(
            selected=True, user=request.user).update(selected=False)
        return redirect('home')


class EnergyInputView(LoginRequiredMixin, FormView):
    template_name = 'energy_input.html'
    form_class = DailyEnergyForm
    success_url = reverse_lazy('home')

    def get_initial(self):
        # fetch the current daily energy object for the current user
        try:
            daily_energy = DailyEnergy.objects.filter(
                user=self.request.user).latest('created_at')
            user_energy = daily_energy.user_energy
        except DailyEnergy.DoesNotExist:
            user_energy = 0

        # return the user energy value as the initial value for the form
        initial = {'user_energy': user_energy}

        return initial

    def form_valid(self, form):
        user_energy = form.cleaned_data['user_energy']
        user = self.request.user

        # gets all the energy input objects made today
        daily_energy_list = DailyEnergy.objects.filter(
            user=user, created_at__date=timezone.now().date())

        # loops through the objects and sets them to the inputted value
        for daily_energy in daily_energy_list:
            daily_energy.user_energy = user_energy
            daily_energy.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            daily_energy = DailyEnergy.objects.filter(
                user=self.request.user).latest('created_at')
            context['daily_energy'] = daily_energy
        except DailyEnergy.DoesNotExist:
            context['daily_energy'] = None

        return context
