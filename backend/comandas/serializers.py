from rest_framework import serializers
from .models import Produto, Comanda, ItemComanda

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco']


class ItemComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemComanda
        fields = ['id', 'comanda', 'produto', 'quantidade']


class ComandaSerializer(serializers.ModelSerializer):
    itens = ItemComandaSerializer(many=True, read_only=True)
    valor_total = serializers.FloatField(read_only=True)
    quantidade_itens = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comanda
        fields = ['id', 'senha', 'nome', 'itens', 'valor_total', 'quantidade_itens']

