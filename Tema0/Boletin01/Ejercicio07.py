numero = int(input("Dime un número para saber si es primo "))

contador = 2

es_primo = True

while numero <= 0:
    numero = int (input)("El número tiene que ser positivo ")

if numero == 1:
    es_primo = False
else:
    while contador < numero and es_primo:
        if numero % contador == 0:
            es_primo = False
        contador += 1

if es_primo:
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo")


