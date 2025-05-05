from data_base import get_database
from usuarios import autenticar_usuario
from productos import obtener_productos

db = get_database()
#colecciones
pedidos_col = db["pedidos"]
stock_col = db["stock"]
productos_col = db["productos"]


def menu_vendedor(usuario_id):
    """Muestra el menú para el vendedor."""
    while True:
        print("\n--- Menú Vendedor ---")
        print("1  Crar Pedido")
        print("2  Mostrar Productos")
        print("3  Cerrar Sesión")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            pedidos = {}
            while True:
                tipo = input("Ingrese el tipo de salmón (1  atlantico, 2  nordico, 3  pacifico) o 'salir' para terminar: ")
                if tipo.lower() == 'salir':
                    break
                kilos = int(input(f"Ingrese la cantidad de kilos para {tipo}: "))
                pedidos[tipo] = kilos
            
            try:
                crear_pedido(usuario_id, pedidos)
            except ValueError as e:
                print(e)
        
        elif opcion == '2':
            obtener_productos()
        
        elif opcion == '3':
            print("Cerrando sesión...")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")



def crear_pedido(usuario_id, pedidos):
    """Crea un nuevo pedido en la base de datos."""
    pedido = {
        "usuario_id": usuario_id,
        "productos": pedidos,
        "total": calcular_total(pedidos),
        "estado": "pendiente"
    }
    pedidos_col.insert_one(pedido)

def calcular_total(pedidos):

    """Calcula el total de un pedido."""
    total = 0
    for tipo, kilos in pedidos.items():
        producto = productos_col.find_one({"tipo": tipo})
        if producto:
            total += producto["valor_venta"] * kilos
    return total

def obtener_productos():
    """Obtiene la lista de productos disponibles."""
    return list(productos_col.find())

def actualizar_stock(tipo, cantidad):
    """Actualiza el stock de un tipo de salmón."""
    productos_col.update_one(
        {"tipo": tipo},
        {"$inc": {"stock": cantidad}}
    )