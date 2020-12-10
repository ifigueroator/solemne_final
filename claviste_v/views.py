from django.shortcuts import render
from mantenedor import templates
from django.http import HttpResponse
from mantenedor.models import registro_cliente

def home(request):
    template = "home.html"
    context = {}    
    return render(request, template, context)

def PlanHogar(request):    
    return render(request, "PlanHogar.html")

def PlanEmpresa(request):    
    return render(request, "PlanEmpresa.html")
 

class FormularioRegCliente(HttpResponse):

    def index(request): 
        registro = regitro_cliente()
        return render(request,"registroCliente.html",{"form":registro})

    def Procesar_registroCliente(request):
        registro = registro_cliente(request.POST)
        if registro.is_valid():
           registro.save()
        registro = registro_cliente()

        return render(request,"registroCliente.html",{"form":registro,"mensaje":'OK'})        
