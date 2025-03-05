from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.db.models import ProtectedError
from ..views import AuthenticationMixin, AuthenticationPasswordMixin
from .forms import UserPasswordChange, UserRegisterForm, UserUpdateForm
from .models import User


class AuthorizationMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object().pk == self.request.user.pk

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
    extra_context = {'title': _('Registration')}
    success_message = _('User was registered successfully.')


class UpdateUser(
    AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User was changed successfully')


# class UpdateUserPassword(
#     AuthentificationMixin, AuthorizationMixin, SuccessMessageMixin, UpdateView):
#     model = User
#     form_class = UserPasswordChange
#     template_name = 'user/update_password.html'
#     success_url = reverse_lazy('users')
#     success_message = _('Password of the user was changed successfully')

class UpdateUserPassword(
    AuthenticationPasswordMixin, SuccessMessageMixin, UpdateView):
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
                self.request, _(
                    "You haven't permission for changing another user."))
        )
        return render(
            request, 'user/update_password.html', {'form': form})


class DeleteUser(
    AuthenticationMixin, AuthorizationMixin, SuccessMessageMixin, DeleteView):
    model = User
    extra_context = {'title': _('Deleting user'), 'button':_("Yes,delete")}
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
