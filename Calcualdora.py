def sumar (num1, num2):
    return num1 + num2

def restar (num1, num2):
    return num1 - num2

def multiplicar (num1, num2):
    return num1 * num2

def dividir (num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero no permitida"

contador = 0
intentos = 5

while contador < intentos:
    print("MENÚ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("ADVERTENCIA: Solo tiene 5 intentos para realizar operaciones")
    print("No desperdices intentos ingresando opciones inválidas")

    opción = input("Seleccione una opción (1-5): ")
    if opción == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", sumar(num1, num2))
        contador += 1
        print(f"Intentos restantes: {intentos - contador}")

    elif opción == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", restar(num1, num2))
        contador += 1
        print(f"Intentos restantes: {intentos - contador}")
        

    elif opción == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print("Resultado:", multiplicar(num1, num2))
        contador += 1
        print(f"Intentos restantes: {intentos - contador}")


    elif opción == "4":
         num1 = float(input("Ingrese el primer número: "))
         num2 = float(input("Ingrese el segundo número: "))
         print("Resultado:", dividir(num1, num2))
         contador += 1
         print(f"Intentos restantes: {intentos - contador}")

    elif opción == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-5).")
        contador += 1
        print(f"Intentos restantes: {intentos - contador}")

if contador >= intentos: 
    print("Se han agotado los intentos. El programa se cerrará.")   
    


