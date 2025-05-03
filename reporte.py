from productos import obtener_pedidos, obtener_ganancias

def generar_reporte_pedidos():
    """Genera un reporte de todos los pedidos realizados."""
    pedidos = obtener_pedidos()
    if not pedidos:
        print("No hay pedidos registrados.")
        return

    print("\n--- Reporte de Pedidos ---")
    for pedido in pedidos:
        print(f"ID de Usuario: {pedido['usuario_id']}, Productos: {pedido['productos']}, Total: ${pedido['total']}, Estado: {pedido['estado']}")

def generar_reporte_ganancias():
    """Genera un reporte de las ganancias por tipo de salmón."""
    ganancias = obtener_ganancias()
    if not ganancias:
        print("No hay ganancias registradas.")
        return

    print("\n--- Reporte de Ganancias ---")
    for tipo, ganancia in ganancias.items():
        print(f"Tipo de salmón: {tipo}, Ganancia: ${ganancia}")

def mostrar_reportes():
    """Muestra los reportes de pedidos y ganancias."""
    while True:
        print("\n--- Menú de Reportes ---")
        print("1    Generar Reporte de Pedidos")
        print("2    Generar Reporte de Ganancias")
        print("3    Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            generar_reporte_pedidos()
        elif opcion == '2':
            generar_reporte_ganancias()
        elif opcion == '3':
            print("Saliendo del menú de reportes...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
