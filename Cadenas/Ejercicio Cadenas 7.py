def IngresoFrase():
    frase = input("Ingresa una frase: ")
    return frase

def BuscaPalabra(frase):
    palabra = input("Ingresa una palabra: ")
    if(palabra.lower() in frase.lower()):
        print("PALABRA ENCONTRADA")
    else:
        print("PALABRA NO ENCONTRADA")
frase = IngresoFrase()
BuscaPalabra(frase)