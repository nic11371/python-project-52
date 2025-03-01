from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from .models import Task
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from ..views import AuthentificationMixin
from django.utils.translation import gettext_lazy as _


class AuthorizationTaskMixin():

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


class TaskMixin(AuthentificationMixin, SuccessMessageMixin):
    model = Task
    extra_context = {'title': _("New task"), 'button': _("Create")}
    success_url = reverse_lazy('tasks')
    fields = ['name', 'description', 'status', 'execute', 'label']


class ListTask(TaskMixin, ListView):
    context_object_name = 'tasks'
    extra_context = {'title': _("Tasks")}
    template_name = 'task/task_list.html'


class CreateTask(TaskMixin, CreateView):
    template_name = 'task/create.html'
    success_message = _("Task created successfully")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ViewTask(TaskMixin, DetailView):
    context_object_name = 'task'
    extra_context = {'title': _('Show task')}


class UpdateTask(TaskMixin, UpdateView):
    success_message = _("Task edited successfully")
    template_name = 'task/update.html'
    extra_context = {'title': _('Tasks'), 'button': _('Edit')}


class DeleteTask(TaskMixin, AuthorizationTaskMixin, DeleteView):
    template_name = 'task/delete.html'
    success_message = _('Task successfully deleted')
