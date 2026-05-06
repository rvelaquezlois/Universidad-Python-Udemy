def IngresoEdad():
    edad = int(input("Ingresa el numero de su edad: "))
    return edad

def EsMayorOMenor(edad):
    if edad >= 18:
        mayor = True
    elif(edad < 18):
        mayor = False
    return mayor

def MuestraResultado(mayor):
    if mayor==True:
        print("Su edad es mayor o igual a 18")
    elif(mayor==False):
        print("Su edad es menor a 18")
    return mayor

#Programa principal
edad = IngresoEdad()
mayor = EsMayorOMenor(edad)
MuestraResultado(mayor)