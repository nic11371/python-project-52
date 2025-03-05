from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..views import AuthenticationMixin, AuthorizationMixin
from .forms import UserRegisterForm
from .models import User


class ListUsers(ListView):
    model = User
    context_object_name = 'users'
    extra_context = {'title': _('Users')}


class SignUpUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = 'general/general_form.html'
    extra_context = {'title': _('Registration'), 'button': _("Sign up")}
    success_message = _('User was registered successfully.')


class UpdateUser(
    AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = User
    extra_context = {
        'title': _('Changing user'),
        'button': _("Change"),
        'link': _("Change password")
    }
    context_object_name = 'update_user'
    template_name = 'general/general_form.html'
    success_url = reverse_lazy('users')
    success_message = _('User was changed successfully')
    fields = ['first_name', 'last_name', 'username']


class UpdateUserPassword(
    AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, PasswordChangeView):
    model = User
    template_name = 'general/general_form.html'
    extra_context = {'title': _('Changing password'), 'button': _("Change")}
    success_url = reverse_lazy('logout')
    success_message = _('Password of the user was changed successfully')


class DeleteUser(
    AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = User
    extra_context = {'title': _('Deleting user'), 'button': _("Yes,delete")}
    template_name = 'general/general_delete_confirm.html'

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, _("User was deleted successfully"))
            return redirect(reverse_lazy('users'))
        except ProtectedError:
            messages.error(
                self.request,
                _("Can't delete, user in use")
            )
            return redirect(reverse_lazy('users'))
