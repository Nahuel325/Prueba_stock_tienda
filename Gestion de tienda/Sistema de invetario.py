"""
Gestion de inventario de una tienda.
1_ Crear un inventario incial usando diccionario.
2_Actualizar el inventario cuando se venden productos.
3_Agregar nuevos productos al inventario.
4_Mostratr un resumen del inventario.
5_Buscar un producto en el inventario y mostrar su cantidad disponible.
6_Gestionar un ciclo de ventas, donde los clientes compran productos hasta que decidas cerrar la tienda.    
"""

#crear el inventario.
inventario = {
    "manzanas":50,
    "naranja":30,
    "peras":20,
    "platanos":10    
}
#Mostrar el inventario.
def mostrar_inventario(invetario):
    print("Invetario actual: ")
    for producto, cantidad in inventario.items():
        print(f"{producto}:{cantidad} unidades")
    
#vender producto
def vender_producto(inventario):
    producto = input("Que producto quieres vender?:").lower()
    cantidad = int(input(f"Cuantas unidades de {producto} quieres vender?: "))
    
    if producto in inventario:
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            print(f"Has vendido {cantidad} unidades de {producto}.")
        else:
            print(f"No hay suficientes {producto} en el inventario.")
            
    else:
        print(f"{producto} No esta en el inventario")


#Agregar nuevos productos de invetarios.
def agregar_producto(inventario):
    producto=input("Introduce el nuevo producto: ").lower()
    cantidad = int(input(f"Introduce la cantidad inicial de {producto}: "))
    
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print (f"Producto {producto} agregado al inventario con {cantidad} unidades.")
    
#Buscar producto en el inventario
def buscar_producto(inventario):
    producto= input("Introduce el nombre del producto que deseas buscar: ").lower()
    
    if producto in inventario:
        print(f"Hay {inventario[producto]} unidades de {producto}.")
    else:
        print(f"{producto} no esta en el inventario.")
        
#Gestion de ventas
def gestion_tienda(inventario):
    while True:
        print("\n Opciones:")
        print("1. Mostrar inventario")
        print("2. Vender producto.")
        print("3. Agregar producto.")
        print("4. Buscar producto.")
        print("5. Cerrar tienda")
        
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            vender_producto(inventario)
        elif opcion == "3":
            agregar_producto(inventario)
        elif opcion == "4":
            buscar_producto(inventario)
        elif opcion == "5":
            print("Cerrando tienda ...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
            
gestion_tienda(inventario)