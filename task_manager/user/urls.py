from django.urls import path
from task_manager.user.views import IndexUserView
from task_manager.user.views import UserFormCreateView


urlpatterns = [
    path('', IndexUserView.as_view(), name="users"),
    path('create/', UserFormCreateView.as_view(), name='user_create')
]
