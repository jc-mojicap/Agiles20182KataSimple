class Estadistica:

    def calcular(self, cadena):
        arreglo = cadena.split(",")
        if len(cadena) == 0:
            return [0, 0]
        else:
            minimo = int(min(arreglo))
            return [len(arreglo), minimo]
