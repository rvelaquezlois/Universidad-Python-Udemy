def IngresaFrase():
    frase = input("Introduce tu frase: ")
    return frase

def ModificaFrase(frase):
    frase_lower = frase.lower()
    frase_upper = frase.upper()
    return frase_lower, frase_upper

def MuestraFrase(frase, frase_lower, frase_upper):
    print(f"""Frase original: {frase}
Frase en minúscula: {frase_lower}
Frase en mayúscula: {frase_upper}""")

frase=IngresaFrase()
frase_lower, frase_upper = ModificaFrase(frase)
MuestraFrase(frase, frase_lower, frase_upper)