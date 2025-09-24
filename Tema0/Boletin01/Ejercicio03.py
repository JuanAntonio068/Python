numero = int(input("Dime un número "))

suma:int = 0
while numero >= 0:
    suma += numero
    numero = int(input("Dime un número "))
print(suma)