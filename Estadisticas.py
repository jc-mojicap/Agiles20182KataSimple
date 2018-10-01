class Estadistica:

    def calcular(self, cadena):
        arreglo = cadena.split(",")
        if len(cadena) == 0:
            return [0, 0, 0, 0]
        else:
            minimo = int(min(arreglo))
            maximo = int(max(arreglo))
            suma = 0
            for elemento in arreglo:
                suma += float(elemento)
            promedio = suma / len(arreglo)
            return [len(arreglo), minimo, maximo, promedio]
