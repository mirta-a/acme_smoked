import bcrypt
from data_base import get_database

db = get_database()


# Colección de productos
productos_col = db["productos"]

# Configuración de los tipos de salmón
tipos_salmon = {
    "1  atlantico": {
        "valor_venta": 5000,
        "costo": 3000
    },
    "2  nordico": {
        "valor_venta": 7000,
        "costo": 4500
    },
    "3  pacifico": {
        "valor_venta": 3000,
        "costo": 1500
    }
}


def agregar_producto(tipo, valor_venta, costo, stock):
    """Agrega un nuevo tipo de salmón a la base de datos."""
    # Verificar si el producto ya existe
    if productos_col.find_one({"tipo": tipo}):
        raise ValueError("El tipo de salmón ya existe.")
    
    # Crear el documento del producto
    nuevo_producto = {
        "tipo": tipo,
        "valor_venta": valor_venta,
        "costo": costo,
        "stock": stock
    }
    
    # Insertar el nuevo producto en la colección
    productos_col.insert_one(nuevo_producto)

def obtener_productos():
    """Devuelve una lista de todos los productos disponibles."""
    return list(productos_col.find({}, {"_id": 0}))  # Excluir el campo _id de los resultados

def actualizar_stock(tipo, cantidad):
    """Actualiza el stock de un tipo de salmón."""
    resultado = productos_col.update_one(
        {"tipo": tipo},
        {"$inc": {"stock": cantidad}}
    )
    return resultado.modified_count > 0

def obtener_producto(tipo):
    """Obtiene la información de un producto específico."""
    return productos_col.find_one({"tipo": tipo}, {"_id": 0})  # Excluir el campo _id

def eliminar_producto(tipo):
    """Elimina un producto de la base de datos."""
    resultado = productos_col.delete_one({"tipo": tipo})
    return resultado.deleted_count > 0


# Colecciones
pedidos_col = db["pedidos"]
productos_col = db["productos"]


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
        {"$inc": {"stock": -cantidad}}
    )

def obtener_pedidos():
    """Obtiene todos los pedidos realizados."""
    return list(pedidos_col.find())

def obtener_ganancias():
    """Calcula las ganancias por tipo de salmón."""
    ganancias = {}
    for pedido in pedidos_col.find():
        for producto in pedido["productos"]:
            tipo = producto["tipo"]
            kilos = producto["kilos"]
            if tipo not in ganancias:
                ganancias[tipo] = 0
            producto_info = productos_col.find_one({"tipo": tipo})
            ganancias[tipo] += (producto_info["valor_venta"] - producto_info["costo"]) * kilos
    return ganancias


