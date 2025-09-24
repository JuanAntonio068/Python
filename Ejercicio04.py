import random


numero_secreto = random.randint(1,101)

numero = int(input("Intenta adivinar el número secreto "))

while numero != numero_secreto and numero != -1:
    if numero > numero_secreto:
        print("Mayor")
    elif numero < numero_secreto:
        print("Menor")
    numero = int(input("Intenta adivinar el número secreto "))

var = "Has ganado" if(numero == numero_secreto) else "Te has rendido"

print(var)