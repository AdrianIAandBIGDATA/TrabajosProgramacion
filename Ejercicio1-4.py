def menu(chainfun):
    for number,item in enumerate(chainfun):
        print(number,":",item)
    option = input("Escribe el numero de la acción: ")
    return option

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
stop=1
while True:
   
 
    chain = ["Introducir valores:", "Sumar", "Restar", "Multiplicar","Dividir","Terminar"]
    option=menu(chain)
    
    if option == "0":
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))
        stop=0
    elif option == "1" and stop==0:
        result = add(a, b)
        print(f"El resultado de la suma es: {result}")
    elif option == "2" and stop==0:
        result = subtract(a, b)
        print(f"El resultado de la resta es: {result}")
    elif option == "3" and stop==0:
        result = multiply(a, b)
        print(f"El resultado de la multiplicación es: {result}")
    elif option == "4" and stop==0:
        result = divide(a, b)
        print(f"El resultado de la división es: {result}")
    elif option == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción incorrecta. Por favor, elige una opción válida o introduzca los datos.")
