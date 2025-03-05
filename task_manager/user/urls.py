from django.urls import path

from .views import (
    DeleteUser,
    ListUsers,
    SignUpUser,
    UpdateUser,
    UpdateUserPassword,
)

urlpatterns = [
    path('', ListUsers.as_view(), name="users"),
    path('create/', SignUpUser.as_view(), name="user_create"),
    path('<int:pk>/update/', UpdateUser.as_view(), name="user_update"),
    path(
        '<int:pk>/update/password/', UpdateUserPassword.as_view(), 
        name="user_update_password"),
    path('<int:pk>/delete/', DeleteUser.as_view(success_url="/users/"), name="user_delete"),
]
