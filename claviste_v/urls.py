from django.contrib import admin
from django.urls import path,include
from mantenedor.views import registroClienteViewset
from rest_framework import routers
from .views import home,PlanHogar,PlanEmpresa,FormularioRegCliente
from django.conf.urls import url



router = routers.DefaultRouter()
router.register('clientes',registroClienteViewset)

urlpatterns = [
    url(r'^$',home,name='home'),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    url(r'^$',PlanHogar,name='PlanHogar'),
    path('PlanHogar/', PlanHogar),
    path('PlanEmpresa/', PlanEmpresa),
    path('RegistroCliente/', FormularioRegCliente.index,name='RegistroCliente'),
    path('guardarRegistroCliente/',FormularioRegCliente.Procesar_registroCliente,name='guardarRegistroCliente'),
]
