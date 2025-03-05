from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View


class AuthenticationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, _("You are not authenticated."))
            )
            return redirect(reverse_lazy("login"))
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AuthorizationMixin(UserPassesTestMixin):

    def test_func(self):
        return self.kwargs.get('pk') == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(
                request,
                messages.error(
                    self.request, _("You haven't permission for changing another user."))
            )
            return redirect(reverse_lazy("users"))
        return super(UserPassesTestMixin, self).dispatch(request, *args, **kwargs)


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'general/general_form.html'
    extra_context = {'title': _("Login"), 'button': _("Sign in")}
    success_message = _('You were login')


class LogoutUser(View):
    def post(self, request, *args, **kwargs):
        return logout(request)

    def get(self, request, *args, **kwargs):
        messages.info(request, _("You were logout"))
        return redirect(reverse_lazy('home'))


def index(request):
    a = None
    a.hello()  # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")
