numero1 = int(input("Dime un número "))
numero2 = int(input("Dime otro número "))

operacion = int(input("Dime la operación a realizar (1 = suma, 2 = resta, 3 = multiplicación, 4 = división): "))

def calculadora(num1, num2, op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

print(calculadora(numero1, numero2, operacion))