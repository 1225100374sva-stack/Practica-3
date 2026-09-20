import time


def mostrar_inventario(inventario):
    """Muestra cada elemento de la lista en formato tabla."""
    if not inventario:
        print("El inventario está vacío.")
        return
    print(f"{'ID':<8}{'IP':<18}{'Clase':<8}{'Estado':<12}")
    print("-" * 46)
    for e in inventario:
        print(f"{e['id']:<8}{e['ip']:<18}{e['clase']:<8}{e['estado']:<12}")


def obtener_clase(ip):
    """Devuelve la clase de una IP según su primer octeto."""
    primer = int(ip.split(".")[0])
    if primer < 128:
        return "A"
    elif primer < 192:
        return "B"
    elif primer < 224:
        return "C"
    elif primer < 240:
        return "D"
    return "E"


def ip_valida(ip):
    """Revisa que la IP tenga 4 números entre 0 y 255."""
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    try:
        return all(0 <= int(p) <= 255 for p in partes)
    except ValueError:
        return False


def agregar_elemento(inventario):
    """Agrega una IP nueva a la lista."""
    id_ip = input("ID: ").strip()
    for e in inventario:
        if e["id"] == id_ip:
            print("Ya existe un elemento con ese ID.")
            return
    ip = input("Dirección IP: ").strip()
    if not ip_valida(ip):
        print("IP inválida.")
        return
    estado = input("Estado (disponible/ocupada): ").strip()
    inventario.append({
        "id": id_ip,
        "ip": ip,
        "clase": obtener_clase(ip),
        "estado": estado,
    })
    print("IP agregada exitosamente.")


def buscar_elemento(inventario):
    """Busca por ID o por IP."""
    dato = input("ID o IP a buscar: ").strip().lower()
    encontrado = False
    for e in inventario:
        if dato in e["id"].lower() or dato in e["ip"]:
            print(e)
            encontrado = True
    if not encontrado:
        print("No se encontró ningún elemento con ese dato.")


def editar_elemento(inventario):
    """Cambia el estado de una IP."""
    id_ip = input("ID del elemento a editar: ").strip()
    for e in inventario:
        if e["id"] == id_ip:
            e["estado"] = input("Nuevo estado: ").strip()
            time.sleep(1)
            print("Elemento actualizado.")
            return
    print("No se encontró un elemento con ese ID.")


def eliminar_elemento(inventario):
    """Elimina una IP por su ID."""
    id_ip = input("ID del elemento a eliminar: ").strip()
    for e in inventario:
        if e["id"] == id_ip:
            inventario.remove(e)
            time.sleep(1)
            print("Elemento eliminado.")
            return
    print("No se encontró un elemento con ese ID.")