from django.urls import path
from task_manager.user.views import IndexUserView


urlpatterns = [
    path('', IndexUserView.as_view(), name="users"),
]
