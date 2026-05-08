def IngresoCaracter():
    caracter = input("Ingresa un caracter: ")
    cantidad = int(input("Ingresa el numero de veces que se va a repetir el caracter: "))
    return caracter,cantidad

def MuestraSecuencia(caracter,cantidad):
    print(caracter*cantidad)

caracter, cantidad = IngresoCaracter()
MuestraSecuencia(caracter,cantidad)