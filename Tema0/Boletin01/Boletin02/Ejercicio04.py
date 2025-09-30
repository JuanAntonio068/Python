# Definir una lista vacía
lista = []

# Rellenar la lista con números introducidos por el usuario
for i in range(0, 10):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

# Ordenar la lista de mayor a menor
lista.sort(reverse=True)

# Imprimir la lista ordenada
print("La lista ordenada de menor a mayor es:", lista)
    