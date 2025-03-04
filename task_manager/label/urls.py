from django.urls import path

from .views import CreateLabel, DeleteLabel, ListLabels, UpdateLabel

urlpatterns = [
    path('', ListLabels.as_view(), name="labels"),
    path('create/', CreateLabel.as_view(), name="label_create"),
    path('<int:pk>/update/', UpdateLabel.as_view(), name="label_update"),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name="label_delete"),
]
