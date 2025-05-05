
from productos import agregar_producto, obtener_productos, actualizar_stock, eliminar_producto
from reporte import generar_reporte_pedidos, generar_reporte_ganancias
from usuarios import obtener_usuarios, actualizar_usuario, eliminar_usuario
from data_base import get_database

# Conexión a la base de datos
db = get_database()

# Colecciones
pedidos_col = db["pedidos"]
stock_col = db["stock"]
productos_col = db["productos"]

def menu_administrador():
    """Muestra el menú para el administrador."""
    while True:
        print("\n--- Menú Administrador ---")
        print("1  Ver Pedidos")
        print("2  Ver Ganancias")
        print("3  Gestionar Usuarios")
        print("4  Gestionar Productos")
        print("5  Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ver_pedidos()
        elif opcion == '2':
            ver_ganancias()
        elif opcion == '3':
            gestionar_usuarios()
        elif opcion == '4':
            gestionar_productos()
        elif opcion == '5':
            print("Cerrando sesión...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def ver_pedidos():
    """Muestra todos los pedidos realizados en la base de datos."""
    pedidos = list(pedidos_col.find())
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    for pedido in pedidos:
        print(f"ID de Usuario: {pedido['usuario_id']}, Productos: {pedido['productos']}, Total: ${pedido['total']}, Estado: {pedido['estado']}")

def ver_ganancias():
    """Muestra las ganancias por tipo de salmón."""
    ganancias = generar_reporte_ganancias()  # Asegúrate de que esta función esté definida
    if not ganancias:
        print("No hay ganancias registradas.")
        return
    for tipo, ganancia in ganancias.items():
        print(f"Tipo de salmón: {tipo}, Ganancia: ${ganancia}")

def gestionar_usuarios():
    """Muestra la lista de usuarios y permite la gestión de sus roles."""
    usuarios = obtener_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(f"Usuario: {usuario['username']}, Rol: {usuario['rol']}")
    
    # Ejemplo de cómo actualizar o eliminar usuarios
    username = input("Ingrese el nombre de usuario para actualizar su rol o eliminarlo: ")
    action = input("¿Desea actualizar el rol (u) o eliminar el usuario (e)? ").lower()
    if action == 'u':
        nuevo_rol = input("Ingrese el nuevo rol (vendedor/administrador): ")
        if actualizar_usuario(username, nuevo_rol):
            print("Rol actualizado exitosamente.")
        else:
            print("No se pudo actualizar el rol. Verifique el nombre de usuario.")
    elif action == 'e':
        if eliminar_usuario(username):
            print("Usuario eliminado exitosamente.")
        else:
            print("No se pudo eliminar el usuario. Verifique el nombre de usuario.")
    else:
        print("Acción no válida.")

def gestionar_productos():
    """Permite agregar o eliminar productos de la base de datos."""
    action = input("¿Desea agregar un nuevo producto (a) o eliminar un producto (e)? ").lower()
    if action == 'a':
        tipo = input("Ingrese el tipo de salmón: ")
        valor_venta = float(input("Ingrese el valor de venta por kilo: "))
        costo = float(input("Ingrese el costo por kilo: "))
        stock = int(input("Ingrese el stock disponible: "))
        try:
            agregar_producto(tipo, valor_venta, costo, stock)
            print("Producto agregado exitosamente.")
        except ValueError as e:
            print(e)
    elif action == 'e':
        tipo = input("Ingrese el tipo de salmón a eliminar: ")
        if eliminar_producto(tipo):
            print("Producto eliminado exitosamente.")
        else:
            print("No se pudo eliminar el producto. Verifique el tipo de salmón.")
    else:
        print("Acción no válida.")

def actualizar_stock(tipo, cantidad):
    """Actualiza el stock en la base de datos."""
    stock_actual = stock_col.find_one({"tipo": tipo})
    if stock_actual:
        nuevo_stock = stock_actual.get("stock_kilos", 0) + cantidad
        stock_col.update_one({"tipo": tipo}, {"$set": {"stock_kilos": nuevo_stock}})
        print(f"El stock de {tipo} ha sido actualizado a {nuevo_stock} kilos.")
    else:
        print(f"No se encontró el tipo de salmón: {tipo}.")

# Llamadas iniciales a las funciones para cargar datos
pedidos = generar_reporte_pedidos()  
ganancias = generar_reporte_ganancias() 
productos = obtener_productos() 
stock = actualizar_stock()

# llamar a menu_administrador() para iniciar el programa
if __name__ == "__main__":
    menu_administrador()