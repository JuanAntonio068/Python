opcion = int(input("Elige una opción \n 1. Agregar ventas \n 2. Calcular total ventas de un producto \n 3. Salir \n"))

# Crear un diccionario vacío para las ventas
ventas = {}

# Mientras la opción no sea 3, seguir pidiendo opciones
while opcion != 3:
    # Si la opción es 1, agregar ventas
    if opcion == 1:
        # Pedir el nombre del producto y la cantidad vendida
        producto = input("Introduce el nombre del producto: ")
        cantidad = int(input("Introduce la cantidad vendida: "))
        # Agregar la cantidad vendida al producto en el diccionario
        if producto in ventas:
            ventas[producto] += cantidad
        # Si el producto no existe, agregarlo al diccionario
        else:
            ventas[producto] = cantidad
    # Si la opción es 2, calcular el total de ventas de un producto
    elif opcion == 2:
        # Pedir el nombre del producto
        producto = input("Introduce el nombre del producto para calcular el total de ventas: ")
        # Mostrar el total de ventas del producto si existe
        if producto in ventas:
            print("El total de ventas de", producto, "es", ventas[producto])
        else:
            print("El producto no existe.")
    # Si la opción es 3, salir del programa
    elif opcion == 3:
        print("Saliendo...")
    else:
        print("Opción no válida.")
    # Volver a pedir una opción    
    opcion = int(input("Elige una opción \n 1. Agregar ventas \n 2. Calcular total ventas de un producto \n 3. Salir \n"))