def ConversionTemperatura():
    temp_celcius = float(input("Ingrese la temperatura de su ciudad: "))
    temp_f = (temp_celcius * 1.8) + 32
    return temp_celcius,temp_f

def MuestraTemperatura(temp_f):
    print("La temperatura en grados Farenheit es de: ",temp_f)

#Programa principal
temp_celcius, temp_f = ConversionTemperatura()
MuestraTemperatura(temp_f)