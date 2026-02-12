class ListaUnidimensional:
    def __init__(self, tamaño):
        self.lista = [0] * tamaño
        self.tamaño = tamaño
    
    def llenar(self, valores):
        for i in range(min(len(valores), self.tamaño)):
            self.lista[i] = valores[i]
    
    def insertar(self, posicion, valor):
        """Inserta un valor en la posición especificada"""
        if 0 <= posicion < self.tamaño:
            self.lista.insert(posicion, valor)
        else:
            print(f"Error: posición {posicion} fuera de rango")
    
    def buscar(self, valor):
        """Busca un valor en la lista y devuelve su índice"""
        try:
            indice = self.lista.index(valor)
            return indice
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
        """Elimina/establece en 0 el elemento en la posición especificada"""
        if 0 <= fila < self.filas and 0 <= columna < self.columnas:
            self.matriz[fila][columna] = 0
        else:
            print(f"Error: posición [{fila}][{columna}] fuera de rango")
    
    def buscar_en_fila(self, fila, valor):
        """Busca un valor en una fila específica y devuelve su índice de columna"""
        if 0 <= fila < self.filas:
            try:
                columna = self.matriz[fila].index(valor)
                return columna
            except ValueError:
                return -1
        else:
            print(f"Error: fila {fila} fuera de rango")
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

print("\n--- Acceso a elementos de las listas ---")
print("\na) Segundo elemento del array unidimensional (índice 1):")
print(f"Elemento: {lista1D.lista[1]}")

print("\nb) Elemento de la segunda fila y segunda columna (índice [1][1]):")
print(f"Elemento: {lista2D.matriz[1][1]}")

print("\n\n--- Inserción y eliminación de elementos ---")
print("\na) Insertando 'Estructura de datos' en la posición 3:")
lista1D.insertar(3, "Estructura de datos")
lista1D.mostrar()

print("\nb) Eliminando el elemento de la tercera fila y tercera columna [2][2]:")
print(f"Elemento antes: {lista2D.matriz[2][2]}")
lista2D.eliminar(2, 2)
print(f"Elemento después:")
lista2D.mostrar()

print("\n\n--- Búsqueda de elementos en arrays ---")
print("\na) Buscando 'Estructura de datos' en el array unidimensional:")
indice = lista1D.buscar("Estructura de datos")
if indice != -1:
    print(f"Elemento encontrado en índice: {indice}")
else:
    print("Elemento no encontrado")

print("\nb) Buscando el valor 5 en la segunda fila (índice 1):")
indice_columna = lista2D.buscar_en_fila(1, 5)
if indice_columna != -1:
    print(f"Elemento encontrado en columna: {indice_columna}")
    print(f"Posición completa: [1][{indice_columna}]")
else:
    print("Elemento no encontrado en esa fila")