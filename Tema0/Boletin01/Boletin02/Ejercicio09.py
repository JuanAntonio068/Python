# Diccionario con las letras y sus puntuaciones
letras = {"A":1, "E":1, "I":1, "O":1, "U":1, "N":1, "S":1, "T":1, "R":1, "L":2, "G":2, "D":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, "Q":5, "J":8, "Ñ":8, "X":8,"K":10, "Z":10}

# Pedir al usuario que introduzca una palabra
palabra = input("Introduce una palabra: ")

# Convertir la palabra a mayúsculas para que coincida con las claves del diccionario
palabra_mayus = palabra.upper()

# Inicializar la puntuación en 0
puntuacion = 0

# Recorrer cada letra de la palabra y sumar su puntuación
for i in range(len(palabra_mayus)):
    # Si la letra está en el diccionario, sumar su puntuación
    if palabra_mayus[i] in letras:
        puntuacion += letras[palabra_mayus[i]]

# Mostrar la puntuación total de la palabra
print("La puntuación de", palabra, "es:", puntuacion)