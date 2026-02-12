class ListaUnidimensional:
    def __init__(self, tamaño):
        self.lista = [0] * tamaño
        self.tamaño = tamaño
    
    def llenar(self, valores):
        for i in range(min(len(valores), self.tamaño)):
            self.lista[i] = valores[i]
    
    def insertar(self, posicion, valor):
        if 0 <= posicion < self.tamaño:
            self.lista.insert(posicion, valor)
    
    def buscar(self, valor):
        try:
            return self.lista.index(valor)
        except ValueError:
            return -1
    
    def mostrar(self):
        print("Lista unidimensional:", self.lista)


class ListaBidimensional:
    def __init__(self, filas, columnas):
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.filas = filas
        self.columnas = columnas
    
    def llenar(self, valores):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = valores[i][j]
    
    def eliminar(self, fila, columna):
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.matriz[fila][columna] = 0
    
    def buscar_en_fila(self, fila, valor):
        if 0 <= fila < self.filas:
            try:
                return self.matriz[fila].index(valor)
            except ValueError:
                return -1
        return -1
    
    def mostrar(self):
        print("Lista bidimensional:")
        for fila in self.matriz:
            print(fila)


lista1D = ListaUnidimensional(5)
lista1D.llenar([10, 20, 30, 40, 50])
lista1D.mostrar()

print()

lista2D = ListaBidimensional(3, 3)
valores = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista2D.llenar(valores)
lista2D.mostrar()

print("\na) Segundo elemento del array:")
print(lista1D.lista[1])

print("\nb) Elemento [1][1]:")
print(lista2D.matriz[1][1])

print("\na) Insertando 'Estructura de datos' en posición 3:")
lista1D.insertar(3, "Estructura de datos")
lista1D.mostrar()

print("\nb) Eliminando elemento [2][2]:")
lista2D.eliminar(2, 2)
lista2D.mostrar()

print("\na) Buscando 'Estructura de datos':")
indice = lista1D.buscar("Estructura de datos")
if indice != -1:
    print(f"Índice: {indice}")

print("\nb) Buscando 5 en fila 1:")
indice_columna = lista2D.buscar_en_fila(1, 5)
if indice_columna != -1:
    print(f"Columna: {indice_columna}")