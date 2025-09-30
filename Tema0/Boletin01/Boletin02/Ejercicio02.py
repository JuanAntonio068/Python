# Crear una lista vacía
lista = []

# Rellenar la lista con números introducidos por el usuario
for i in range(0, 10):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

# Inicializar las variables máximo y mínimo en el primer elemento de la lista
maximo = lista[0]
minimo = lista[0]

# Recoorer la lista para encontrar el máximo y el mínimo
for i in range(0, 10):

    # Comparar cada elemento de la lista con las variables máximo y mínimo
    if lista[i] < minimo:
        minimo = lista[i]
    
    if lista[i] > maximo:
        maximo = lista[i]

# Imprimir los resultados
print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)