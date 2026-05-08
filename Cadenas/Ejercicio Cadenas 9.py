def IngresoNumeroTarjeta():
    numero = input("Ingresa los 16 numeros de tu tarjeta: ")
    return numero

def Logica(numero):
    n_slide = numero[-4:]
    n_escondido = f"{"*"*12}{n_slide}"
    return n_escondido

def Confirmacion(n_escondido):
    respuesta = input(f"Los últimos cuatro dígitos de su tarjeta son {n_escondido} ¿Es correcto?\t")
    if(respuesta.lower() == "s"):
        print("BIENVENIDO")
    else:
        print("Intente nuevamente")

numero = IngresoNumeroTarjeta()
n_escondido = Logica(numero)
Confirmacion(n_escondido)