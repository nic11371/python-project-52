from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .models import CustomUser
from .forms import UserRegisterForm, LoginForm, \
    UserUpdateForm, UserPasswordChange, UserDeleteForm
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexUserView(View):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserRegisterForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, _("User was registered successfully.")
            )
            return redirect(reverse('login'))
        return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserUpdateForm(instance=user)
        return render(
            request, 'users/update.html', {'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _("User was changed successfully"))
            return redirect(reverse('users'))
        return render(
            request, 'users/update.html', {'form': form, 'user_id': user_id})


class UserFormUpdatePasswordView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserPasswordChange(user)
        return render(
            request, 'users/update_password.html', {
                'form': form, 'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserPasswordChange(user, request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, _("Password of the user was changed successfully")
            )
            return redirect(reverse('users'))
        return render(
            request, 'users/update_password.html', {'form': form})


class UserFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        form = UserDeleteForm(user)
        return render(
            request, 'users/delete.html', {
                'form': form, 'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        messages.success(request, _("User was deleted successfully"))
        return redirect(reverse('users'))


class LoginUserView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _("You were logined"))
                return redirect(reverse('home'))
        return render(request, 'users/login.html', {'form': form})


class LogoutUserView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _("You were logouted"))
        return redirect(reverse('home'))
