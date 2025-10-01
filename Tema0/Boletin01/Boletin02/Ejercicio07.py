# Declarar la variable opcion y pedir al usuario que elija una opción
opcion = int(input("Elige una opción \n 1. Agregar contacto \n 2. Eliminar contacto \n 3. Buscar contacto \n 4. Salir \n"))

# Crear un diccionario vacío para la agenda
agenda = {}

# Mientras la opción no sea 4, seguir pidiendo opciones
while opcion != 4:
    # Si la opción es 1, agregar un contacto
    if opcion == 1:
        # Pedir el nombre y el teléfono del contacto
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")
        # Agregar el contacto a la agenda
        agenda[nombre] = telefono
    # Si la opción es 2, eliminar un contacto
    elif opcion == 2:
        # Pedir el nombre del contacto a eliminar
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        # Eliminar el contacto de la agenda si existe
        if nombre in agenda:
            del agenda[nombre]
            print("Contacto eliminado.")
        else:
            print("El contacto no existe.")
    # Si la opción es 3, buscar un contacto
    elif opcion == 3:
        # Pedir el nombre del contacto a buscar
        nombre = input("Introduce el nombre del contacto a buscar: ")
        # Mostrar el teléfono del contacto si existe
        if nombre in agenda:
            print("El teléfono de", nombre, "es", agenda[nombre])
        else:
            print("El contacto no existe.")
    # Si la opción es 4, salir del programa
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Opción no válida.")
    # Volver a pedir una opción
    opcion = int(input("Elige una opción \n 1. Agregar contacto \n 2. Eliminar contacto \n 3. Buscar contacto \n 4. Salir \n"))
