from unittest import TestCase

from Estadisticas import Estadistica


class Test(TestCase):

    def test_stringVacio(self):
        self.assertEqual(Estadistica().calcular(""), [0, 0], "String vacio")

    def test_stringUnElemento(self):
        self.assertEqual(Estadistica().calcular("1"), [1, 1], "String con un elemento")

    def test_stringDosElementos(self):
        self.assertEqual(Estadistica().calcular("1,2"), [2, 1], "String con dos elemento")

    def test_stringVariosElementos1(self):
        self.assertEqual(Estadistica().calcular("1,2,3"), [3, 1], "String con tres elemento")

    def test_stringVariosElementos2(self):
        self.assertEqual(Estadistica().calcular("1,2,3,4"), [4, 1], "String con cuatro elemento")
