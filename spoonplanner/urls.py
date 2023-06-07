from django.contrib import admin
from django.urls import path, include
from schedule.views import TaskListView, TaskCreateView, TaskCompleteView
from schedule.views import TaskDeleteView, TaskDeleteConfirmView
from schedule.views import TaskSelectView, HomeView, ClearTodaysTasks
from schedule.views import TaskUpdateView, EnergyInputView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('<int:pk>/delete/confirm/', TaskDeleteConfirmView.as_view(),
         name='task-confirm-delete'),
    path('<int:pk>/complete/', TaskCompleteView.as_view(),
         name='task-complete'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/select/', TaskSelectView.as_view(), name='task-select'),
    path('clear_selected/', ClearTodaysTasks.as_view(), name='clear-selected'),
    path('energy_input/', EnergyInputView.as_view(), name='energy-input'),
    path('', HomeView.as_view(), name='home'),
]
