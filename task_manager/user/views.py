from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views import View
from .models import CustomUser
from .forms import UserForm
from .forms import LoginForm
from django.urls import reverse


class IndexUserView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        return render(request, 'users/create.html', {'form': form})


class LoginUserView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            if user is not None:
                login(request, user)
                return redirect('users/')
            else:
                return render(request, 'users/login.html')
        else:
            form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class LogoutUserView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('login'))
