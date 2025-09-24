caracter = input("Ingrese un caracter: ")

def es_vocal(c: str):
    vocales = "aeiouAEIOU"
    return c in vocales

if es_vocal(caracter):
    print(f"{caracter} es una vocal.")
else:
    print(f"{caracter} no es una vocal.")