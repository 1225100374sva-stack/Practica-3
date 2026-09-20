import json

ARCHIVO_DATOS = "ip.json"


def cargar_datos():
    """Carga la lista de IPs desde el archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado, se iniciará vacío.")
        return []
    except json.JSONDecodeError:
        print("El archivo está vacío o dañado, se iniciará vacío.")
        return []


def guardar_datos(inventario):
    """Guarda la lista de IPs en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)