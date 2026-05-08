def IngresoDatos():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    provincia = input("Ingresa tu provincia: ")
    return nombre, edad, provincia

def MuestraDatos(nombre, edad, provincia):
    print(f"Nombre: \"{nombre}\"\nEdad: {edad}\nCiudad: {provincia}")

nombre, edad, provincia = IngresoDatos()
MuestraDatos(nombre, edad, provincia)☺