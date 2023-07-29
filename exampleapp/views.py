import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


# Create your views here.

class Index(APIView):

    def get(self, request):
        return Response({
            "now": f"{not datetime.datetime.utcnow()}",
            "message": "This is a public resource"
        })


class IndexProtected(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "now": f"{not datetime.datetime.utcnow()}",
            "message": "This is a protected resource"
        })
