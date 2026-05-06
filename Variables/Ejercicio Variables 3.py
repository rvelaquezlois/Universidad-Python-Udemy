def pedir_datos():
    nombre = input("Ingresá tu nombre: ")
    edad = int(input("Ingresá tu edad: "))
    altura = float(input("Ingresá tu altura (en metros): "))

    return nombre, edad, altura


def mostrar_datos(nombre, edad, altura):
    print(f"Hola, soy {nombre}, tengo {edad} años y mido {altura} metros.")


# Programa principal
nombre, edad, altura = pedir_datos()
mostrar_datos(nombre, edad, altura)