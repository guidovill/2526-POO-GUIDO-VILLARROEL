class Producto:
    """
    Clase Producto (requisito):
    Atributos: ID (único), nombre, cantidad, precio.
    Métodos: obtener y establecer atributos (getters/setters).
    """

    def __init__(self, producto_id, nombre, cantidad, precio):
        self._id = None
        self._nombre = None
        self._cantidad = None
        self._precio = None

        self.set_id(producto_id)
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)
        self.set_precio(precio)

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_id(self, producto_id):
        producto_id = str(producto_id).strip()
        if not producto_id:
            raise ValueError("El ID no puede estar vacío.")
        self._id = producto_id

    def set_nombre(self, nombre):
        nombre = str(nombre).strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        try:
            cantidad = int(cantidad)
        except ValueError:
            raise ValueError("La cantidad debe ser un entero.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def set_precio(self, precio):
        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser numérico (ej: 1.25).")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    # Tupla (colección) para mostrar/serializar
    def como_tupla(self):
        return (self._id, self._nombre, self._cantidad, self._precio)