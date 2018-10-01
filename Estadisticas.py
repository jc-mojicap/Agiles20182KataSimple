class Estadistica:

    def calcular(self, cadena):
        arreglo = cadena.split(",")
        if len(cadena) == 0:
            return 0
        else:
            return len(arreglo)
