def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
a=0
b=0
while True:
   
    print("\nSelecciona una opción:")
    print("0. Introducir valores:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Terminar")

    option = input("Escribe el numero de la acción: ")
    if option == "0":
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))
    elif option == "1":
        result = add(a, b)
        print(f"El resultado de la suma es: {result}")
    elif option == "2":
        result = subtract(a, b)
        print(f"El resultado de la resta es: {result}")
    elif option == "3":
        result = multiply(a, b)
        print(f"El resultado de la multiplicación es: {result}")
    elif option == "4":
        result = divide(a, b)
        print(f"El resultado de la división es: {result}")
    elif option == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción incorrecta. Por favor, elige una opción válida.")
