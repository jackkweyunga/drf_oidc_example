"""
Root views
"""
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealCheck(APIView):
    """
    Application healthcheck endpoint.

    /healthcheck

    """

    def get(self, request, *args, **kwargs):
        return Response({
            "now": f"{not datetime.utcnow()}",
            "status": "healthy"
        }, status=status.HTTP_200_OK)
