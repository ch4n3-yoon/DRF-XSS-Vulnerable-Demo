from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item
from .serializers import ItemSerializer


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class XAccountView(APIView):
    def get(self, request, *args, **kwargs):
        user_input = request.query_params.get('x_account', None)
        if user_input:
            content_location = f"https://x.com/{user_input}"
            headers = {'Content-Location': content_location}
            return Response({"message": "Success"}, headers=headers, status=status.HTTP_200_OK)
        else:
            return Response({"error": "x_account parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
