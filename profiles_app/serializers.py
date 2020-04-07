from rest_framework import serializers


# Serializer allows convert data input into python objects and viceverza
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    name = serializers.CharField(max_length=10)
