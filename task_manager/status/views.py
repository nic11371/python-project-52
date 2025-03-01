from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from .models import Status
from django.db.models import ProtectedError
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from ..views import AuthentificationMixin


class StatusMixin(AuthentificationMixin, SuccessMessageMixin):
    model = Status
    extra_context = {'title': _("Statuses"), 'button': _("create")}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('statuses')
    fields = ['status_name']


class ListStatuses(StatusMixin, ListView):
    context_object_name = 'statuses'


class CreateStatus(StatusMixin, CreateView):
    success_message = _("Status created successfully")
    template_name = 'status/create.html'


class UpdateStatus(StatusMixin, UpdateView):
    success_message = _("Status created successfully")
    template_name = 'status/update.html'
    extra_context = {'title': _('Statuses'), 'button': _('Change')}


class DeleteStatus(StatusMixin, DeleteView):
    template_name = 'status/delete.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, _("Status was deleted successfully"))
            return redirect(reverse_lazy('statuses'))
        except ProtectedError:
            messages.error(
                self.request,
                _("Error! Can't delete, status in use")
            )
            return redirect(reverse_lazy('statuses'))
