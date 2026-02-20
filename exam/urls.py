from django.urls import path
from .views import UserCreateView, UserListView

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/create/", UserCreateView.as_view()),
]
