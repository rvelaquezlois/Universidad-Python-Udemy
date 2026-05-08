def IngresoEmail():
    email = input("Ingresa tu email: ")
    return email

def Logica(email):
    indice = email.find("@")
    if(indice != -1):
        find_arroba = True
    else:
        find_arroba = False
    if(email[-4:]==".com"):
        find_com = True
    else:
        find_com = False

    return find_arroba,find_com

def ValidezEmail(find_arroba,find_com):
    if((find_arroba==True) and (find_com==True)):
        print("MAIL VALIDO")
    else:
        print("MAIL INVALIDO")

email = IngresoEmail()
Logica(email)
find_arroba,find_com = Logica(email)
ValidezEmail(find_arroba,find_com)

