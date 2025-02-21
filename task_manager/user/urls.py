from django.urls import path
from .views import IndexUserView
from .views import UserFormCreateView
from .views import LoginUserView
from .views import LogoutUserView
from django.contrib.auth import views as auth_views
from .forms import LoginForm


urlpatterns = [
    path('', IndexUserView.as_view(), name="users"),
    path('create/', UserFormCreateView.as_view(), name="user_create"),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html', next_page='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='users/login'), name='logout'),
]
