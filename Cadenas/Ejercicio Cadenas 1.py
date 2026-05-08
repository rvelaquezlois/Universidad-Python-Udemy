def IngresoDeDatos():
    print("***"*3+" INGRESO DE DATOS "+"***"*3)
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    nombre_completo = f"{nombre} {apellido}"
    empresa = input("Ingresa tu empresa: ")
    dominio = input("Ingresa tu dominio: ")
    return nombre, apellido, nombre_completo, empresa, dominio

def GeneradorEmail(nombre, apellido, nombre_completo, empresa, dominio):
    if(dominio[0:1]!="."):
        dominio = f".{dominio}"
    nombre_lower = nombre.lower()
    apellido_lower = apellido.lower()
    empresa_lower = empresa.lower()
    dominio_lower = dominio.lower()
    usuario = f"{nombre_lower}.{apellido_lower}"
    empr_dominio = f"@{empresa_lower}{dominio_lower}"
    email = f"{usuario}{empr_dominio}"
    return usuario, email

def MuestraDatos(nombre_completo, usuario, email):
    print(f"Bienvenido {nombre_completo}. \n Su usuario es: {usuario} \n Su email es: {email}")
nombre,apellido,nombre_completo,empresa,dominio = IngresoDeDatos()
usuario, email = GeneradorEmail(nombre, apellido, nombre_completo, empresa, dominio)
MuestraDatos(nombre_completo, usuario, email)