from usuarios import autenticar_usuario
from vendedor import realizar_pedido, mostrar_productos
from administrador import ver_pedidos, ver_ganancias, gestionar_usuarios, gestionar_productos


def menu_vendedor(usuario_id):
    """Muestra el menú para el vendedor."""
    while True:
        print("\n--- Menú Vendedor ---")
        print("1  Realizar Pedido")
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
                realizar_pedido(usuario_id, pedidos)
            except ValueError as e:
                print(e)
        
        elif opcion == '2':
            mostrar_productos()
        
        elif opcion == '3':
            print("Cerrando sesión...")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


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



def main():
    """Función principal que inicia la aplicación."""
    while True:
        print("\n--- Sistema de Pedidos de Salmón ---")
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        
        rol = autenticar_usuario(nombre_usuario, password)
        
        if rol == 'vendedor':
            print("Inicio de sesión exitoso como vendedor.")
            menu_vendedor(nombre_usuario)
        
        elif rol == 'administrador':
            print("Inicio de sesión exitoso como administrador.")
            menu_administrador()
        
        else:
            print("Credenciales incorrectas. Intente nuevamente.")
if __name__ == "__main__":
    main()
