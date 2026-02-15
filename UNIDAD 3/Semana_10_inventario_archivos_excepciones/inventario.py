import csv
from pathlib import Path
from producto import Producto


class Inventario:
    """
    Inventario basado en LISTA (requisito).
    Mejora Semana 10:
    - Guarda/lee inventario en archivo de texto inventario.txt
    - Maneja excepciones: FileNotFoundError, PermissionError
    - Crea inventario.txt si no existe
    """

    CAMPOS = ["id", "nombre", "cantidad", "precio"]

    def __init__(self, nombre_archivo: str = "inventario.txt"):
        self.__productos: list[Producto] = []

        # inventario.txt se guarda en la MISMA carpeta de esta Semana 10
        base_dir = Path(__file__).resolve().parent
        self.__ruta = base_dir / nombre_archivo

        self.__mensaje_inicio = ""
        self.__cargar_desde_archivo()

    def get_mensaje_inicio(self) -> str:
        return self.__mensaje_inicio

    # -------------------------
    # Utilidades (lista)
    # -------------------------
    def id_existe(self, producto_id: str) -> bool:
        producto_id = str(producto_id).strip()
        for p in self.__productos:
            if p.get_id() == producto_id:
                return True
        return False

    def obtener_todos(self) -> list[Producto]:
        return list(self.__productos)

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        texto = texto.strip().lower()
        resultados: list[Producto] = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():  # parcial + insensible a mayúsculas
                resultados.append(p)
        return resultados

    # -------------------------
    # Archivos (cargar/guardar)
    # -------------------------
    def __crear_archivo_si_no_existe(self) -> None:
        if not self.__ruta.exists():
            with self.__ruta.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
                writer.writeheader()

    def __cargar_desde_archivo(self) -> None:
        try:
            self.__crear_archivo_si_no_existe()

            with self.__ruta.open("r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                # Caso archivo corrupto/sin cabecera
                if reader.fieldnames is None or any(c not in reader.fieldnames for c in self.CAMPOS):
                    self.__productos.clear()
                    self.__crear_archivo_si_no_existe()
                    self.__mensaje_inicio = "⚠️ inventario.txt estaba vacío o corrupto. Se reinició correctamente."
                    return

                cargados = 0
                ignorados = 0
                self.__productos.clear()

                for row in reader:
                    try:
                        producto_id = str(row.get("id", "")).strip()
                        nombre = str(row.get("nombre", "")).strip()
                        cantidad = int(row.get("cantidad", "0"))
                        precio = float(row.get("precio", "0"))

                        if not producto_id or not nombre:
                            ignorados += 1
                            continue

                        # Evita IDs duplicados al cargar
                        if self.id_existe(producto_id):
                            ignorados += 1
                            continue

                        self.__productos.append(Producto(producto_id, nombre, cantidad, precio))
                        cargados += 1

                    except (ValueError, TypeError):
                        ignorados += 1

                if cargados == 0:
                    self.__mensaje_inicio = "📁 inventario.txt listo (sin productos guardados aún)."
                else:
                    extra = f" | ⚠️ líneas ignoradas: {ignorados}" if ignorados else ""
                    self.__mensaje_inicio = f"✅ Inventario cargado: {cargados} producto(s){extra}"

        except FileNotFoundError:
            # Requisito: si no existe, crearlo
            self.__crear_archivo_si_no_existe()
            self.__mensaje_inicio = "⚠️ No existía inventario.txt, se creó uno nuevo."
        except PermissionError:
            self.__mensaje_inicio = "❌ Sin permisos para leer/crear inventario.txt (PermissionError)."
        except OSError as e:
            self.__mensaje_inicio = f"❌ Error del sistema al leer inventario.txt: {e}"

    def __guardar_en_archivo(self) -> tuple[bool, str]:
        try:
            self.__crear_archivo_si_no_existe()

            with self.__ruta.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
                writer.writeheader()
                for p in self.__productos:
                    writer.writerow(p.to_record())

            return True, "✅ Cambios guardados correctamente en inventario.txt."

        except FileNotFoundError:
            # Intento: crear y guardar nuevamente
            try:
                self.__crear_archivo_si_no_existe()
                with self.__ruta.open("w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
                    writer.writeheader()
                    for p in self.__productos:
                        writer.writerow(p.to_record())
                return True, "⚠️ inventario.txt no existía; se creó y se guardaron los cambios."
            except Exception as e:
                return False, f"❌ No se pudo crear/guardar inventario.txt: {e}"

        except PermissionError:
            return False, "❌ No se pudo guardar: no tiene permisos (PermissionError)."
        except OSError as e:
            return False, f"❌ Error del sistema al guardar inventario.txt: {e}"

    # -------------------------
    # Operaciones CRUD (lista)
    # -------------------------
    def anadir_producto(self, producto: Producto) -> tuple[bool, str]:
        if self.id_existe(producto.get_id()):
            return False, "❌ Error: ese ID ya existe. No se añadió el producto."

        self.__productos.append(producto)
        ok, msg = self.__guardar_en_archivo()
        if not ok:
            # Revertir si no pudo guardar
            self.__productos.pop()
            return False, msg
        return True, f"✅ Producto añadido. {msg}"

    def eliminar_producto_por_id(self, producto_id: str) -> tuple[bool, str]:
        producto_id = str(producto_id).strip()

        for i, p in enumerate(self.__productos):
            if p.get_id() == producto_id:
                eliminado = self.__productos.pop(i)
                ok, msg = self.__guardar_en_archivo()
                if not ok:
                    # Revertir si falla el guardado
                    self.__productos.insert(i, eliminado)
                    return False, msg
                return True, f"✅ Producto eliminado. {msg}"

        return False, "⚠️ No se encontró un producto con ese ID."

    def actualizar_producto_por_id(
        self,
        producto_id: str,
        nueva_cantidad: int | None = None,
        nuevo_precio: float | None = None,
    ) -> tuple[bool, str]:
        producto_id = str(producto_id).strip()

        for p in self.__productos:
            if p.get_id() == producto_id:
                # Backup para revertir
                old_cantidad = p.get_cantidad()
                old_precio = p.get_precio()

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                ok, msg = self.__guardar_en_archivo()
                if not ok:
                    # Revertir si falla
                    p.set_cantidad(old_cantidad)
                    p.set_precio(old_precio)
                    return False, msg

                return True, f"✅ Producto actualizado. {msg}"

        return False, "⚠️ No se encontró un producto con ese ID."