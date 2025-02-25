from django.urls import path
from .views import IndexStatusView
from .views import StatusCreateView
from .views import StatusUpdateView
from .views import StatusDeleteView


urlpatterns = [
    path('', IndexStatusView.as_view(), name="statuses"),
    path('create/', StatusCreateView.as_view(), name="status_create"),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name="status_update"),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name="status_delete"),
]
