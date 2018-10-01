from unittest import TestCase

from Estadisticas import Estadistica


class Test(TestCase):

    def test_stringVacio(self):
        self.assertEqual(Estadistica().calcular(""), [0, 0, 0, 0], "String vacio")

    def test_stringUnElemento(self):
        self.assertEqual(Estadistica().calcular("1"), [1, 1, 1, 1], "String con un elemento")

    def test_stringDosElementos(self):
        self.assertEqual(Estadistica().calcular("1,2"), [2, 1, 2, 1.5], "String con dos elemento")
        
