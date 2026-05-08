def IngresaPalabra():
    palabra = input("Ingresa la palabra: ")
    return palabra

def MuestraPalabraSlice(palabra):
    print(f"Primeras tres letras: {palabra[0:3]}, últimas tres letras: {palabra[-3:]}")
palabra = IngresaPalabra()
MuestraPalabraSlice(palabra)