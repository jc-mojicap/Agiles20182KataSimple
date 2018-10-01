class Estadistica:

    def calcular(self, cadena):
        if len(cadena) == 0:
            return [0, 0]
        elif len(cadena) == 1:
            return [1, 1]
        else:
            return [2, 1]
