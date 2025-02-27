from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class TaskMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    extra_context = {'title': _("New task"), 'button': _("Create")}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('tasks')
    fields = ['task_name', 'description', 'status', 'execute', 'marks']


class ListTask(TaskMixin, ListView):
    context_object_name = 'tasks'
    extra_context = {'title': _("Tasks")}
    template_name = 'task/tasks_list.html'


class CreateTask(TaskMixin, CreateView):
    success_message = _("Task created successfully")
    template_name = 'task/create.html'


class ViewTask(TaskMixin, DetailView):
    context_object_name = 'task'
    extra_context = {'title': _('Show task')}


class UpdateTask(TaskMixin, UpdateView):
    success_message = _("Task edited successfully")
    template_name = 'task/update.html'
    extra_context = {'title': _('Tasks'), 'button': _('Edit')}


class DeleteTask(TaskMixin, DeleteView):
    template_name = 'task/delete.html'
    success_message = _('Task successfully deleted')

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, _("Task was deleted successfully"))
            return redirect(reverse_lazy('statuses'))
        except ProtectedError:
            messages.error(
                self.request,
                _("Error! Can't delete, task in use")
            )
            return redirect(reverse_lazy('statuses'))
