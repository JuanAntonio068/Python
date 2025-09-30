import random

# Generar una lista
lista =[]

# Rellenar la lista con números aleatorios
for i in range(0, 10):
    lista.append(random.randint(1,100))

# Imprimir la lista generada
print(lista)