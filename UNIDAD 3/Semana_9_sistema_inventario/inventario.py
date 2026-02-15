from producto import Producto


class Inventario:
    def __init__(self):
        # Lista de productos (estructura pedida)
        self.__productos: list[Producto] = []

    def id_existe(self, producto_id: str) -> bool:
        # Verifica si el ID ya está registrado
        for p in self.__productos:
            if p.get_id() == producto_id:
                return True
        return False

    def anadir_producto(self, producto: Producto) -> bool:
        # Retorna True si se añadió, False si el ID ya existía
        if self.id_existe(producto.get_id()):
            return False
        self.__productos.append(producto)
        return True

    def eliminar_producto_por_id(self, producto_id: str) -> bool:
        # Retorna True si se eliminó, False si no se encontró
        for i, p in enumerate(self.__productos):
            if p.get_id() == producto_id:
                del self.__productos[i]
                return True
        return False

    def actualizar_producto_por_id(self, producto_id: str, nueva_cantidad: int | None = None, nuevo_precio: float | None = None) -> bool:
        # Se permite actualizar cantidad, precio o ambos
        for p in self.__productos:
            if p.get_id() == producto_id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return True
        return False

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        # Búsqueda parcial e insensible a mayúsculas (para nombres similares)
        texto = texto.strip().lower()
        resultados: list[Producto] = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def obtener_todos(self) -> list[Producto]:
        # Devuelve copia para evitar modificaciones externas directas
        return list(self.__productos)
