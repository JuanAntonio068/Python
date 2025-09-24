numero1 = int(input("Dime un numero "))

numero2 = int(input("Dime otro número "))

if numero1 > numero2:
    print(str(numero2) + " < " + str(numero1))
elif numero1 < numero2:
    print(str(numero1) + " < " + str(numero2))
else:
    print("Los números son iguales")