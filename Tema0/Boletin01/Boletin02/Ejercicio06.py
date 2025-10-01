# Creamos la variable texto y le pedimos al usuario que introduzca un texto
texto = input("Escribe un texto: ")

# Convertimos el texto a minúsculas y lo separamos en palabras
palabras = texto.lower().split()

# Creamos un diccionario vacío para guardar las frecuencias
frecuencias = {}

# Recorremos cada palabra y contamos cuántas veces aparece
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] = frecuencias[palabra] + 1
    else:
        frecuencias[palabra] = 1

# Mostramos el resultado
print("Frecuencia de palabras:")
for palabra in frecuencias:
    print(palabra, ":", frecuencias[palabra])