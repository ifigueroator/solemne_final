from django.shortcuts import render

from rest_framework import viewsets
from mantenedor.models import registro_cliente

from claviste_v.serializers import registroClienteSerializers
#api rest
class registroClienteViewset(viewsets.ModelViewSet):
    queryset = registro_cliente.objects.all()
    serializer_class=registroClienteSerializers

# Create your views here.
