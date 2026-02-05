from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("role/", views.create_role, name="create_role"),
    path("operation/", views.create_operation, name="create_operation"),
    path("user/", views.create_user, name="create_user"),
]
