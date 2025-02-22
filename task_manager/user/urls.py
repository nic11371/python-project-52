from django.urls import path
from .views import IndexUserView
from .views import UserFormCreateView
from .views import UserFormUpdateView
from .views import UserFormDeleteView
from .views import LoginUserView
from .views import LogoutUserView


urlpatterns = [
    path('', IndexUserView.as_view(), name="users"),
    path('create/', UserFormCreateView.as_view(), name="user_create"),
    path('<int:pk>/update/', UserFormUpdateView.as_view(), name="user_update"),
path('<int:pk>/delete/', UserFormDeleteView.as_view(), name="user_delete"),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
