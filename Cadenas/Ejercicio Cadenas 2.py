def IngresoDatos():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    provincia = input("Ingresa tu provincia: ")
    return nombre, edad, provincia

def MuestraDatos(nombre, edad, provincia):
    print(f"""Hola {nombre}
Tu edad es de {edad}
Vivís en {provincia}""")

nombre, edad, provincia = IngresoDatos()
MuestraDatos(nombre, edad, provincia)