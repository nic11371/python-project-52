from django.shortcuts import render, redirect
from .models import User
from django.views.generic import CreateView, ListView, \
    UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm, \
    UserUpdateForm, UserPasswordChange, UserDeleteForm
from django.urls import reverse_lazy
from django.contrib import messages
from ..views import AuthentificationMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext_lazy as _


class AuthorizationMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().username == self.request.user.username

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(
                request,
                messages.error(
                    self.request, _("You haven't permission for changing another user."))
            )
            return redirect(reverse_lazy("users"))
        return super(UserPassesTestMixin, self).dispatch(request, *args, **kwargs)


class ListUsers(ListView):
    model = User
    context_object_name = 'users'
    extra_context = {'title': _('Users')}


class SignUpUser(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = 'user/create.html'
    extra_context = {'title': _('Create user')}
    success_message = _('User was registered successfully.')


class UpdateUser(AuthentificationMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('users')
    success_message = 'User was changed successfully'


class UpdateUserPassword(AuthentificationMixin, SuccessMessageMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserPasswordChange(user)
        return render(
            request, 'user/update_password.html', {
                'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserPasswordChange(user, request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, _("Password of the user was changed successfully")
            )
            return redirect(reverse_lazy('users'))
        messages.error(
            request,
            messages.error(
                self.request, _("You haven't permission for changing another user."))
        )
        return render(
            request, 'user/update_password.html', {'form': form})


class DeleteUser(AuthentificationMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('users')
    success_message = 'User was deleted successfully'
