from productos import obtener_pedidos, obtener_ganancias, agregar_producto, eliminar_producto
from usuarios import obtener_usuarios, actualizar_usuario, eliminar_usuario



def ver_pedidos():
    """Muestra todos los pedidos realizados en la base de datos."""
    pedidos = obtener_pedidos()
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    for pedido in pedidos:
        print(f"ID de Usuario: {pedido['usuario_id']}, Productos: {pedido['productos']}, Total: ${pedido['total']}, Estado: {pedido['estado']}")


def ver_ganancias():
    """Muestra las ganancias por tipo de salmón."""
    ganancias = obtener_ganancias()
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
