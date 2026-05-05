print("*** SISTEMA DE TIENDA ONLINE ***")

nombre_producto = "iPhone 16 Pro Max"
precio_producto = 1400.00
cantidad_inventario = 15
HAY_STOCK = False

if cantidad_inventario > 0:
    HAY_STOCK = True

print("Producto: ",nombre_producto)
print("Precio producto $",precio_producto)
print("¿Hay stock?",HAY_STOCK)
print("Cantidad en el inventario: ",cantidad_inventario)

nombre_producto = "iPhone 17"
precio_producto = 2189.54
HAY_STOCK = False
cantidad_inventario = 0

if cantidad_inventario > 0:
    HAY_STOCK = True


print("Producto: ",nombre_producto)
print("Precio producto $",precio_producto)
print("¿Hay stock?",HAY_STOCK)
print("Cantidad en el inventario: ",cantidad_inventario)