from django.test import TestCase
from django.contrib.auth.models import User
from mantenedor.models import registro_cliente,nuevos_plan

class MantenedorTestCase(TestCase):
        def setUp(self):
            userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
            )

class registroClienteTestCase(TestCase):
    def setUp(self):
        registro_cliente.objects.create(nombre='Felipe',apellidoP="Munoz")
        registro_cliente.objects.create(nombre='Ivan',apellidoP="Figueroa")     

    def test_campos_cliente_correctos(self):
        obj1 = registro_cliente.objects.get(nombre='Felipe')
        obj2 = registro_cliente.objects.get(nombre='Ivan')
        self.assertEqual(obj1.nombre,'Felipe')
        self.assertEqual(obj2.nombre,'Ivan')
        self.assertEqual(obj1.apellidoP,'Munoz')
        self.assertEqual(obj2.apellidoP,'Figueroa')
"""
class registroPlanTestCase(TestCase):
    def setUp1(self):
        nuevos_plan.objects.create(nombre_plan='Hogar',precio_plan=14900)
        nuevos_plan.objects.create(nombre_plan='Empresa',precio_plan=19900)     

    def test_campos_plan_correctos(self):
        obj3 = nuevos_plan.objects.get(nombre_plan='Hogar')
        obj4 = nuevos_plan.objects.get(nombre_plan='Empresa')
        self.assertEqual(obj3.nombre_plan,'Hogar')
        self.assertEqual(obj4.nombre_plan,'Empresa')
        self.assertEqual(obj3.precio_plan,14900)
        self.assertEqual(obj4.precio_plan,19900)   """     



# Create your tests here.
