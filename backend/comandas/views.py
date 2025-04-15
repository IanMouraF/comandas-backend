from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Comanda, Produto, ItemComanda
from .serializers import ComandaSerializer, ProdutoSerializer, ItemComandaSerializer
from rest_framework.views import APIView


class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    

class ItemComandaListCreateView(generics.ListCreateAPIView):
    queryset = ItemComanda.objects.all()
    serializer_class = ItemComandaSerializer

    def delete(self, request, *args, **kwargs):
        ItemComanda.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProdutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


# Create your views here.
class ComandaListCreateView(generics.ListCreateAPIView):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer

    def delete(self, request, *args, **kwargs):
        Comanda.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ComandaPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer
    lookup_field = "pk"

