import time
from datos import cargar_datos, guardar_datos
from operaciones import (
    mostrar_inventario,
    agregar_elemento,
    buscar_elemento,
    editar_elemento,
    eliminar_elemento,
)

ANCHO = 30


def mostrar_menu():
    """Muestra el menú principal con formato decorado."""
    opciones = [
        "1. Agregar una IP",
        "2. Mostrar todas las IPs",
        "3. Buscar una IP",
        "4. Editar estado de una IP",
        "5. Eliminar una IP",
        "6. Guardar y salir",
    ]
    print("\n╔" + "═" * ANCHO + "╗")
    print("║" + "BÓVEDA DE IPs".center(ANCHO) + "║")
    print("╠" + "═" * ANCHO + "╣")
    for op in opciones:
        print("║ " + op.ljust(ANCHO - 1) + "║")
    print("╚" + "═" * ANCHO + "╝")


def main():
    """Función principal: muestra el menú y maneja la interacción."""
    inventario = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            agregar_elemento(inventario)
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            buscar_elemento(inventario)
        elif opcion == "4":
            editar_elemento(inventario)
        elif opcion == "5":
            eliminar_elemento(inventario)
        elif opcion == "6":
            guardar_datos(inventario)
            print("Inventario guardado. Saliendo del programa.")
            break
        else:
            print("Opción inválida. Seleccione una opción válida.")
        time.sleep(1)


if __name__ == "__main__":
    main()