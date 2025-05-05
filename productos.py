import bcrypt
from data_base import get_database

db = get_database()


# Colecciones
productos_col = db["productos"]
stock_col = db["stock"]

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
    if not tipo or not isinstance(valor_venta, (int, float)) or not isinstance(costo, (int, float)) or not isinstance(stock, int):
        raise ValueError("Parámetros inválidos. Asegúrate de que 'tipo' no esté vacío y que 'valor_venta', 'costo' sean números y 'stock' sea un entero.")
    
    if productos_col.find_one({"tipo": tipo}):
        raise ValueError("El tipo de salmón ya existe.")
    
    nuevo_producto = {
        "tipo": tipo,
        "valor_venta": valor_venta,
        "costo": costo,
        "stock": stock
    }
    
    try:
        productos_col.insert_one(nuevo_producto)
    except Exception as e:
        raise Exception(f"Error al agregar el producto: {e}")

def obtener_productos():
    """Devuelve una lista de todos los productos disponibles."""
    try:
        return list(productos_col.find({}, {"_id": 0}))  # Excluir el campo _id de los resultados
    except Exception as e:
        raise Exception(f"Error al obtener productos: {e}")

def actualizar_stock(tipo, cantidad):
    """Actualiza el stock de un tipo de salmón."""
    if not isinstance(cantidad, int):
        raise ValueError("La cantidad debe ser un entero.")
    
    resultado = productos_col.update_one(
        {"tipo": tipo},
        {"$inc": {"stock": cantidad}}
    )
    
    if resultado.matched_count == 0:
        raise ValueError("El tipo de salmón no existe.")
    
    return resultado.modified_count > 0

def eliminar_producto(tipo):
    """Elimina un producto de la base de datos."""
    resultado = productos_col.delete_one({"tipo": tipo})
    if resultado.deleted_count == 0:
        raise ValueError("El tipo de salmón no existe.")
    
    return True

# crear stock inicial
def crear_stock():
    if stock_col.count_documents({}) == 0:
        
        salmones = [
            {"tipo": "Atlántico", "precio_venta": 5000, "costo": 3000, "stock_kilos": 150},
            {"tipo": "Nórdico", "precio_venta": 7000, "costo": 4500, "stock_kilos": 100},
            {"tipo": "Pacífico", "precio_venta": 3000, "costo": 1500, "stock_kilos": 200}
        ]
        stock_col.insert_many(salmones)
        print("Stock inicial creado.")
    else:
        print("Stock ya ingresado.")

if __name__ == "__main__":
       crear_stock()  
