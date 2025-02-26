from django.urls import path
from .views import ListStatuses
from .views import CreateStatus
from .views import UpdateStatus
from .views import DeleteStatus


urlpatterns = [
    path('', ListStatuses.as_view(), name="statuses"),
    path('create/', CreateStatus.as_view(), name="status_create"),
    path('<int:pk>/update/', UpdateStatus.as_view(), name="status_update"),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name="status_delete"),
]
