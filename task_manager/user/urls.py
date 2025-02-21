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
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
