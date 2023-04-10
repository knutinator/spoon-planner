from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()  # accesses the method of the parent class
        queryset = queryset.filter(user=self.request.user)  # only gets the tasks in the database created by the current user
        return queryset


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'energy']
    success_url = reverse_lazy('task-list')
    template_name = 'task_create.html'

    def form_valid(self, form):  # marks the created task with the current username
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'energy']
    template_name = 'task_edit.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')

class TaskDeleteConfirmView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'task_confirm_delete.html'
