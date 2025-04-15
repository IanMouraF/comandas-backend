from django.urls import path
from . import views

urlpatterns = [
    path('comandas/', views.ComandaListCreateView.as_view(), name='comanda-view-create'),
    path('comandas/<int:pk>/', 
        views.ComandaPostRetrieveUpdateDestroy.as_view(), 
        name='update'),
    path('produtos/', views.ProdutoListCreateView.as_view(), name='produto-list-create'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto-detail'),
    path('itens-comanda/', views.ItemComandaListCreateView.as_view(), name='item-comanda-list-create'),
    path('itens-comanda/<int:pk>/', views.ItemComandaListCreateView.as_view(), name='item-comanda-detail'),
]
