from rest_framework.views import APIView
from rest_framework.response import Response 


class HelloApiView(APIView):
    # Test API View
    def get(self, request, format = None):
        # Returns a lis of APIView features
        an_apiview = [
            'Uses HTTP methods (get, post, parch, put, delete)',
            'Traditional Django View',
            'Gives you the most control over you app',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
