
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test rest_framework ApiView """

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods such as (get, post, update, patch, delete)',
            'Is similar to traditional Django Views',
            'Gives you most control over your Applications',
            'Is mapped manually to the URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    