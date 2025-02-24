from django.urls import path
from .views import IndexUserView
from .views import UserFormCreateView
from .views import UserFormUpdateView
from .views import UserFormUpdatePasswordView
from .views import UserFormDeleteView


urlpatterns = [
    path('', IndexUserView.as_view(), name="users"),
    path('create/', UserFormCreateView.as_view(), name="user_create"),
    path('<int:pk>/update/', UserFormUpdateView.as_view(), name="user_update"),
    path('<int:pk>/password/', UserFormUpdatePasswordView.as_view(), name="user_update_password"),
    path('<int:pk>/delete/', UserFormDeleteView.as_view(), name="user_delete"),
]
