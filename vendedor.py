from data_base import get_database
from productos import crear_pedido, obtener_productos, actualizar_stock

db = get_database()



def realizar_pedido(usuario_id, pedidos):
    """
    Realiza un nuevo pedido de salmón.
    
    :param usuario_id: ID del vendedor que realiza el pedido.
    :param pedidos: Diccionario con los tipos de salmón y la cantidad en kilos.
    """
    # Verificar que el pedido tiene entre 1 y 3 tipos de salmón
    if len(pedidos) < 1 or len(pedidos) > 3:
        raise ValueError("El pedido debe contener entre 1 y 3 tipos de salmón.")
    
    # Obtener productos disponibles
    productos_disponibles = obtener_productos()
    tipos_disponibles = {producto['tipo']: producto for producto in productos_disponibles}
    
    # Verificar que todos los tipos de salmón en el pedido son válidos
    for tipo, kilos in pedidos.items():
        if tipo not in tipos_disponibles:
            raise ValueError(f"Tipo de salmón '{tipo}' no disponible.")
        if kilos <= 0:
            raise ValueError("La cantidad de kilos debe ser mayor a cero.")
        if tipos_disponibles[tipo]['stock'] < kilos:
            raise ValueError(f"No hay suficiente stock para '{tipo}'. Stock disponible: {tipos_disponibles[tipo]['stock']}.")
    
    # Crear el pedido
    crear_pedido(usuario_id, pedidos)
    
    # Actualizar el stock de cada tipo de salmón
    for tipo, kilos in pedidos.items():
        actualizar_stock(tipo, -kilos)
    print("Pedido realizado exitosamente.")

def mostrar_productos():
    """Muestra todos los productos de salmón disponibles."""
    productos = obtener_productos()
    for producto in productos:
        print(f"Tipo: {producto['tipo']}, Precio por kilo: ${producto['valor_venta']}, Stock: {producto['stock']}")
