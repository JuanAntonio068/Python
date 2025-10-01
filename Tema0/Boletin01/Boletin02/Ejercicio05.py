# importar la librería random para generar números aleatorios
import random

# Definir una lista vacía
lista = []

# Contador para contar las apariciones del número n
contador_n = 0

# Rellenar la lista con números aleatorios entre 1 y 10
for i in range(0, 100):
    lista.append(random.randint(1,10))

# Pedir al usuario que introduzca un número entre 1 y 100
n = int(input("Introduce un número entre 1 y 100: para contar cuántas veces aparece en la lista: "))

# Contar cuántas veces aparece el número n en la lista
for i in range(0, 100):
    if lista[i] == n:
        contador_n += 1

# Mostrar el resultado
print("El número", n, "aparece", contador_n, "veces en la lista.")