# Definir una lista vacía
lista = []

# Rellenar la lista con números introducidos por el usuario
for i in range(0, 8):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

# Recorrer la lista para determinar si cada número es par o impar
for i in range(0, 8):
    if lista[i] % 2 == 0:
        print(f"El número {lista[i]} es par")
    else:
        print(f"El número {lista[i]} es impar")

