from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from ..views import AuthenticationMixin
from .filters import TaskFilter
from .forms import TaskForm
from .models import Task


class AuthorizationTaskMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().author.pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(
                request,
                messages.error(
                    self.request, _("The task can only be deleted by its author."))
            )
            return redirect(reverse_lazy("tasks"))
        return super().dispatch(request, *args, **kwargs)


class TaskMixin(AuthenticationMixin, SuccessMessageMixin):
    model = Task
    extra_context = {'title': _("Tasks"), 'button': _("Create task")}
    success_url = reverse_lazy('tasks')


class ListTask(TaskMixin, FilterView):
    context_object_name = 'tasks'
    extra_context = {'title': _("Tasks"), 'button': _("Create task")}
    template_name = 'task/task_list.html'
    filterset_class = TaskFilter


class CreateTask(TaskMixin, CreateView):
    success_message = _("Task created successfully")
    extra_context = {'title': _("Create task"), 'button': _("Create")}
    template_name = 'general/general_form.html'
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ViewTask(TaskMixin, DetailView):
    context_object_name = 'task'
    extra_context = {'title': _('Show task')}


class UpdateTask(TaskMixin, UpdateView):
    success_message = _("Task edited successfully")
    extra_context = {'title': _('Changing task'), 'button': _('Change')}
    template_name = 'general/general_form.html'
    form_class = TaskForm


class DeleteTask(TaskMixin, AuthorizationTaskMixin, DeleteView):
    extra_context = {'title': _('Deleting task'), 'button': _('Yes, delete')}
    success_message = _('Task successfully deleted')
    template_name = 'general/general_delete_confirm.html'
