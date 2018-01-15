from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

class HelloApiView(APIView):
    """Test ApiView"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """
        Get View
        """
        an_apiview = [
            'Uses HTTP method as function (get,post, patch, put, delete)',
            'similar Django View ',
            'Gives you the most control over your logic',
            'Urls manually'
        ]
        return Response({
            "message": "Hello",
            "an_apiview": an_apiview
        })

    def post(self, request):
        """ 
        Create a hello message with our name
        """

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ 
        Updating an object
        """
        return Response({
            'method': "Put"
        })

    def patch(self, request, pk=None):
        """
        Updating partial object
        """
        return Response({
            'method': "Patch"
        })
    
    def delete(self, request, pk=None):
        """
        Delete object
        """
        return Response({
            'method': "Delete"
        })