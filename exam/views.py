from .models import User
from rest_framework import generics
from .serializers import UserSerializer



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by("-user_id")
    serializer_class = UserSerializer