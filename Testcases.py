from unittest import TestCase

from Estadisticas import Estadistica


class Test(TestCase):

    def test_stringVacio(self):
        self.assertEqual(Estadistica().calcular(""), 0, "String vacio")

    def test_stringUnElemento(self):
        self.assertEqual(Estadistica().calcular("1"), 1, "String con un elemento")