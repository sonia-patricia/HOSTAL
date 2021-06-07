from django.urls import path
from website import views
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('clientes', views.clientes, name='clientes'),
    path('clientes/list', views.ClienteListView.as_view(), name='clientes_list'),
    path('cliente/<int:pk>', views.ClienteDetailView.as_view(), name='cliente-detail'),

    path('cliente/create', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update', views.ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/<int:pk>/delete', views.ClienteDelete.as_view(), name='cliente_delete'),
]