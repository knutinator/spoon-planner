from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()  # accesses the method of the parent class
        queryset = queryset.filter(user=self.request.user)  # gets only the tasks in the database created by the current user
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'energy', 'completed']
    success_url = reverse_lazy('task-list')
    template_name = 'task_create.html'

    def form_valid(self, form):  # marks the created task with the current username
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
        return redirect('task-list')


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
            selected_tasks = Task.objects.filter(selected=True)
            context['selected_tasks'] = selected_tasks
        return context
