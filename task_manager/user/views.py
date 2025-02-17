from django.shortcuts import render, redirect
from django.views import View
from task_manager.user.models import User
from task_manager.user.forms import UserForm
from task_manager.user.forms import LoginForm


class IndexUserView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
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
            return redirect('login')
        return render(request, 'user/create.html', {'form': form})


class LoginUserView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'users/login.html', {'form': form})
