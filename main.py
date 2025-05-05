from usuarios import autenticar_usuario
from vendedor import menu_vendedor, realizar_pedido, mostrar_productos
from administrador import menu_administrador, ver_pedidos, ver_ganancias, gestionar_usuarios, gestionar_productos



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
