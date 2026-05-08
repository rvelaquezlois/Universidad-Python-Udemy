def IngresaNombre():
    nombre = input("Ingresa tu nombre: ")
    return nombre

def MuestraLongitud(nombre):
    print("La longitud de su nombre es de: ", len(nombre)," caracteres")

nombre = IngresaNombre()
MuestraLongitud(nombre)