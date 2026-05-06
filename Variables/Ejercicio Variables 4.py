#Cálculo de precio con IVA
#Definí una constante para el IVA (por ejemplo 21%).
#Pedile al usuario que ingrese el precio de un producto y mostrá el precio final con IVA incluido.

IVA = 0.21

def IngresoPrecio():
    precio = float(input("Ingresa el precio del producto: "))
    precio_total = (precio * IVA)+precio
    return precio, precio_total

def PrecioConIva(precio_total):
     print("El precio del producto con IVA es de: ",precio_total)

#Programa principal
precio, precio_total = IngresoPrecio()
PrecioConIva(precio_total)