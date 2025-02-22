from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views import View
from .models import CustomUser
from .forms import UserCreateForm, LoginForm
from django.urls import reverse


class IndexUserView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserCreateForm(instance=user)
        return render(
            request, 'users/update.html', {'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('users'))
        return render(
            request, 'users/update.html', {'form': form, 'user_id': user_id})


class UserFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect(reverse('users'))


class LoginUserView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
        return render(request, 'users/login.html', {'form': form})


class LogoutUserView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))
