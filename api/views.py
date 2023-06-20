from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from notes.models import Note
from django.contrib.auth.models import User
from .serializers import UserSerializer, MyTokenObtainPairSerializer, NoteSerializer


class APIHomePageView(APIView):
  def get(self, request):
    routes = [
      "api/token",
      "api/token/refresh/",
      "api/token/verify/",
      "api/token/blacklist/",
      "api/notes/all",
      "api/notes/update/<int:pk>",
      "api/notes/delete/<int:pk>",
      "api/notes/retrieve/<int:pk>",
      "api/account/signup",
      "api/account/update",
      "api/account/delete",
    ]
    return Response(routes)


class UserCreateAPIView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    obj = super().get_object()
    if obj != self.request.user:
      raise permissions.PermissionDenied
    return obj


class UserDeleteAPIView(generics.DestroyAPIView):
  queryset = User.objects.all()
  permission_classes = [permissions.IsAuthenticated]

  def get_object(self):
    obj = super().get_object() 
    if obj != self.request.user:
      raise permissions.PermissionDenied
    return obj


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer


class NoteCreateAPIView(generics.CreateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class NoteListAPIView(generics.ListAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    user_id = self.request.user.id
    return Note.objects.filter(user_id=user_id)


class NoteUpdateAPIView(generics.UpdateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    user_id = self.request.user.id
    return Note.objects.filter(user_id=user_id)


class NoteDeleteAPIView(generics.DestroyAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    user_id = self.request.user.id
    return Note.objects.filter(user_id=user_id)

class NoteRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    user_id = self.request.user.id
    return Note.objects.filter(user_id=user_id)