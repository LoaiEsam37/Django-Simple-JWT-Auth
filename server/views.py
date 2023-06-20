from rest_framework.response import Response
from rest_framework.decorators import APIView

class HomePageView(APIView):
  def get(self, request):
    routes = [
      "api",
      "admin/",
    ]
    return Response(routes)