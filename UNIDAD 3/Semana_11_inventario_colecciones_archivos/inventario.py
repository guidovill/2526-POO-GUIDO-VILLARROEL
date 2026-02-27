import json
import os

from producto import Producto


class Inventario:
    """
    Clase Inventario (requisito):
    - Usa una colección adecuada (diccionario) para almacenar productos por ID:
      productos = { "P001": Producto, "P002": Producto, ... }

    Integración de colecciones (requisito):
    - Diccionario: almacenamiento principal por ID (búsqueda rápida).
    - Lista: para devolver listados (mostrar todos / resultados de búsqueda).
    - Conjunto (set): para evitar duplicados al buscar por nombre (IDs encontrados).
    - Tupla: cada Producto se representa como tupla (id, nombre, cantidad, precio).
    """

    def __init__(self, archivo="inventario.txt"):
        self.productos = {}  # diccionario principal {id: Producto}
        self.archivo = archivo
        self.cargar()

    # ---------- Operaciones requeridas ----------
    def anadir_producto(self, producto):
        pid = producto.get_id()
        if pid in self.productos:
            return False
        self.productos[pid] = producto
        self.guardar()
        return True

    def eliminar_producto_por_id(self, producto_id):
        producto_id = str(producto_id).strip()
        if producto_id not in self.productos:
            return False
        del self.productos[producto_id]
        self.guardar()
        return True

    def actualizar_cantidad(self, producto_id, nueva_cantidad):
        producto_id = str(producto_id).strip()
        if producto_id not in self.productos:
            return False
        self.productos[producto_id].set_cantidad(nueva_cantidad)
        self.guardar()
        return True

    def actualizar_precio(self, producto_id, nuevo_precio):
        producto_id = str(producto_id).strip()
        if producto_id not in self.productos:
            return False
        self.productos[producto_id].set_precio(nuevo_precio)
        self.guardar()
        return True

    def buscar_y_mostrar_por_nombre(self, texto):
        """
        Búsqueda por nombre (requisito).
        Parcial e insensible a mayúsculas.
        Devuelve una lista de productos encontrados.
        """
        texto = str(texto).strip().lower()
        if not texto:
            return []

        ids_encontrados = set()  # conjunto para evitar duplicados
        for pid, prod in self.productos.items():
            if texto in prod.get_nombre().lower():
                ids_encontrados.add(pid)

        resultados = []  # lista
        for pid in ids_encontrados:
            resultados.append(self.productos[pid])

        resultados.sort(key=lambda p: (p.get_nombre().lower(), p.get_id()))
        return resultados

    def mostrar_todos(self):
        """
        Mostrar todos los productos (requisito).
        Devuelve lista ordenada.
        """
        lista_productos = list(self.productos.values())  # lista
        lista_productos.sort(key=lambda p: (p.get_nombre().lower(), p.get_id()))
        return lista_productos

    # ---------- Archivos (requisito: serialización / deserialización) ----------
    def guardar(self):
        """
        Serialización:
        Se transforma el diccionario de productos en un diccionario serializable,
        usando tuplas de Producto (convertidas a lista para JSON).
        """
        data = {"productos": {}}
        for pid, prod in self.productos.items():
            tupla = prod.como_tupla()            # tupla
            data["productos"][pid] = list(tupla) # JSON no guarda tuplas: se guarda como lista

        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: no se pudo escribir el archivo (PermissionError).")

    def cargar(self):
        """
        Deserialización:
        Se lee el archivo y se reconstruye el diccionario {id: Producto}.
        """
        if not os.path.exists(self.archivo):
            # Si no existe el archivo, se inicia vacío y se guarda uno nuevo
            self.guardar()
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.productos = {}
            productos_guardados = data.get("productos", {})

            for pid, lista_datos in productos_guardados.items():
                # lista_datos viene como [id, nombre, cantidad, precio]
                producto_id = str(lista_datos[0]).strip()
                nombre = str(lista_datos[1]).strip()
                cantidad = int(lista_datos[2])
                precio = float(lista_datos[3])

                prod = Producto(producto_id, nombre, cantidad, precio)
                self.productos[pid] = prod

        except PermissionError:
            print("Error: no se pudo leer el archivo (PermissionError).")
        except json.JSONDecodeError:
            print("Error: el archivo está dañado. Se iniciará inventario vacío.")
            self.productos = {}
            self.guardar()