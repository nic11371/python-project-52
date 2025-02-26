from django.urls import path
from .views import ListUsers
from .views import SignUpUser
from .views import UpdateUser
from .views import UpdateUserPassword
from .views import DeleteUser


urlpatterns = [
    path('', ListUsers.as_view(), name="users"),
    path('create/', SignUpUser.as_view(), name="user_create"),
    path('<int:pk>/update/', UpdateUser.as_view(), name="user_update"),
    path('<int:pk>/password/', UpdateUserPassword.as_view(), name="user_update_password"),
    path('<int:pk>/delete/', DeleteUser.as_view(), name="user_delete"),
]
