from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app import serializers


class ProfileApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Request a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an api view': an_apiview})

    def post(self, request):
        """Create a hello message with given name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)