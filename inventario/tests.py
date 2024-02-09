from django.test import TestCase 
from .models import Equipo

class EquipoListViewTestCase(TestCase):  
    def test_my_view(self):  
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    

equipo_mock = {
    "referencia":"referencia 1",
    "marca":"marca 1",
    "procesador":"m1",
    "memoria":"8gb",
    "disco":"520Gb",
    "tipo":"Mesa"
}
class EquipoModelTest(TestCase):
    def setUp(self):
        self.test_equipo = Equipo(**equipo_mock)
        self.test_equipo.save()

    def test_referencia(self):
        self.assertEquals(str(self.test_equipo), equipo_mock["referencia"])

    def test_marca(self):
        self.assertEquals(self.test_equipo.marca, equipo_mock["marca"])

    def test_procesador(self):
        self.assertEquals(self.test_equipo.procesador, equipo_mock["procesador"])

    def test_memoria(self):
        self.assertEquals(self.test_equipo.memoria, equipo_mock["memoria"])
    
    def test_disco(self):
        self.assertEquals(self.test_equipo.disco, equipo_mock["disco"])

    def test_tipo(self):
        self.assertEquals(self.test_equipo.tipo, equipo_mock["tipo"])

    def test_get_by_id(self):
        self.assertEquals(Equipo.objects.get(pk=1), self.test_equipo)
    
    def test_get_all(self):
        equipos = Equipo.objects.all()
        self.assertEquals(equipos.count(), 1)

    def tearDown(self):
        self.test_equipo.delete()


