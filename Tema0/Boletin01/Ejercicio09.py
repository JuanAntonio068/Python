numero1 = int(input("Dime un número "))
numero2 = int(input("Dime otro número "))

def numeros_entre(num1, num2):
    if num1 < num2:
        for i in range(num1 + 1, num2):
            print(i)
    elif num1 > num2:
        for i in range(num2 + 1, num1):
            print(i)
    else:
        print("Los números son iguales")

numeros_entre(numero1, numero2)