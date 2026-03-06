"""
Clase Usuario
- Mantiene una LISTA de libros prestados (se guarda el ISBN en lista para ser práctico y claro).
"""

class Usuario:
    def __init__(self, nombre: str, user_id: str):
        if not nombre or not user_id:
            raise ValueError("Nombre e ID de usuario son obligatorios.")

        self.nombre = nombre.strip()
        self.user_id = user_id.strip()

        # Lista de ISBNs prestados actualmente
        self.libros_prestados: list[str] = []

    def prestar_isbn(self, isbn: str) -> bool:
        isbn = isbn.strip()
        if not isbn:
            return False

        if isbn in self.libros_prestados:
            return False

        self.libros_prestados.append(isbn)
        return True

    def devolver_isbn(self, isbn: str) -> bool:
        isbn = isbn.strip()
        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)
            return True
        return False

    def tiene_prestamos(self) -> bool:
        return len(self.libros_prestados) > 0

    def __str__(self) -> str:
        return f"{self.nombre} (ID: {self.user_id})"

    def __repr__(self) -> str:
        return f"Usuario(nombre={self.nombre!r}, user_id={self.user_id!r}, libros_prestados={self.libros_prestados!r})"