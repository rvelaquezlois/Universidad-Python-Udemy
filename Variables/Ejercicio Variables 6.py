def LeeNumero():
    num1 = int(input("Ingresa el primer numero entero: "))
    num2 = int(input("Ingresa el segundo numero entero: "))
    return num1, num2

def Operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, multiplicacion, division

def MuestraResultados(suma, resta, multiplicacion, division):
    print("La suma es: ",suma)
    print("La resta es: ",resta)
    print("La multiplicacion es: ",multiplicacion)
    print("La division es: ",division)

 #Programa principal
num1, num2 = LeeNumero()
suma, resta, multiplicacion, division = Operaciones(num1, num2)
MuestraResultados(suma, resta, multiplicacion, division)