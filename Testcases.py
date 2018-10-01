from unittest import TestCase

from Estadisticas import Estadistica


class Test(TestCase):

    def test_stringVacio(self):
        self.assertEqual(Estadistica().calcular(""), [0, 0, 0], "String vacio")
