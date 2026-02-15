class Producto:
    """
    Clase Producto (POO) para representar un ítem del inventario.
    ID se maneja como texto (str) por flexibilidad.
    """

    def __init__(self, producto_id: str, nombre: str, cantidad: int, precio: float):
        self.__id = str(producto_id).strip()
        self.__nombre = str(nombre).strip()
        self.__cantidad = int(cantidad)
        self.__precio = float(precio)

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = str(nuevo_nombre).strip()

    def set_cantidad(self, nueva_cantidad: int) -> None:
        self.__cantidad = int(nueva_cantidad)

    def set_precio(self, nuevo_precio: float) -> None:
        self.__precio = float(nuevo_precio)

    def to_record(self) -> dict:
        # Registro de texto para guardar en inventario.txt
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": str(self.__cantidad),
            "precio": str(self.__precio),
        }

    def __str__(self) -> str:
        return (
            f"ID: {self.__id} | Nombre: {self.__nombre} | "
            f"Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"
        )