numero = int(input("Dime un número para calcular su factorial "))

factorial:int = 1

for i in range(numero, 0, -1):
    factorial *= i

print("El factorial de " + str(numero) + " es: " + str(factorial))

