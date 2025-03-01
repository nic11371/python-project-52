from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _


class AuthentificationMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                messages.error(self.request, _("You are not authenticated."))
            )
            return redirect(reverse_lazy("login"))
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _("You were logined"))
                return redirect(reverse_lazy('home'))
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _("You were logouted"))
        return redirect(reverse_lazy('home'))
