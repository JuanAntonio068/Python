diccionario = {'e': 'p', 'i': 'v', 'k': 'i', 'm': 'u', 'p': 'm', 'q': 't', 'r': 'e', 's': 'r', 't': 'k', 'u': 'q', 'v': 's'}

frase = input("Dime una frase para encriptarla: ")

frase_minus = frase.lower()

frase_encripatada = ""
for i in range(len(frase_minus)):
    if frase_minus[i] in diccionario:
        frase_encripatada += diccionario[frase_minus[i]]
    else:
        frase_encripatada += frase_minus[i]
print("La frase encriptada es:", frase_encripatada)