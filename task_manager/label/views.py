from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..views import AuthentificationMixin
from .models import Label


class LabelMixin(AuthentificationMixin, SuccessMessageMixin):
    model = Label
    extra_context = {'title': _("Labels"), 'button': _("Create")}
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('labels')
    fields = ['name']


class ListLabels(LabelMixin, ListView):
    context_object_name = 'labels'


class CreateLabel(LabelMixin, CreateView):
    success_message = _("Label created successfully")
    template_name = 'label/create.html'


class UpdateLabel(LabelMixin, UpdateView):
    success_message = _("Label created successfully")
    template_name = 'label/update.html'
    extra_context = {'title': _('Labels'), 'button': _('Change')}


class DeleteLabel(LabelMixin, DeleteView):
    template_name = 'label/delete.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, _("Label was deleted successfully"))
            return redirect(reverse_lazy('labels'))
        except ProtectedError:
            messages.error(
                self.request,
                _("Can't delete, label in use")
            )
            return redirect(reverse_lazy('labels'))
