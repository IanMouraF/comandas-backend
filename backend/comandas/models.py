from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class Comanda(models.Model):
    senha = models.CharField(max_length=10, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"Comanda {self.senha} - {self.nome}"

    @property
    def valor_total(self):
        return sum(item.subtotal for item in self.itens.all())

    @property
    def quantidade_itens(self):
        return sum(item.quantidade for item in self.itens.all())


class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade
