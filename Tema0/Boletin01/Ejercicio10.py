numero1 = int(input("Dime un número "))
numero2 = int(input("Dime otro número "))

def maximo(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "Los números son iguales"

print(maximo(numero1, numero2))