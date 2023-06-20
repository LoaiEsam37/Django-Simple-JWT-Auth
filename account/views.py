from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


@api_view(["GET"])
def get_csrf(request):
  response = JsonResponse({"Info": "Set - CSRF Cookie"})
  response["X-CSRFToken"] = get_token(request)
  return response

@api_view(["POST"])
def login_user(request):
  csrf_token = request.headers.get('X-CSRFToken')

  parser = JSONParser()
  data = parser.parse(request)
  username = data.get("username")
  password = data.get("password")

  if username is None or password is None:
    return Response({"Info": "Username and Password are needed"}, status=400)

  user = authenticate(username=username, password=password)

  if user is None:
    return Response({"Info": "User doesn`t exist"}, status=400)

  login(request, user)
  return Response({"Info": "User logged in successfully"}, status=200)
