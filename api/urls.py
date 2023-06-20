from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView
from .views import (
  APIHomePageView,
  MyTokenObtainPairView,
  NoteListAPIView,
  NoteUpdateAPIView,
  NoteDeleteAPIView,
  NoteRetrieveAPIView,
  UserCreateAPIView,
  UserDeleteAPIView,
  NoteCreateAPIView,
)

urlpatterns = [
    path('', APIHomePageView.as_view()),
    path('token/', MyTokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('token/blacklist/', TokenBlacklistView.as_view()),
    path('notes/all/', NoteListAPIView.as_view()),
    path('api/notes/create/', NoteCreateAPIView.as_view()),
    path('api/notes/update/<int:pk>/', NoteUpdateAPIView.as_view()),
    path('api/notes/delete/<int:pk>/', NoteDeleteAPIView.as_view()),
    path('api/notes/retrieve/<int:pk>/', NoteRetrieveAPIView.as_view()),
    path('account/signup/', UserCreateAPIView.as_view()),
    path('account/delete/', UserDeleteAPIView.as_view()),
]
