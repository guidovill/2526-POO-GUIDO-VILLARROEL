"""
Clase Biblioteca
Requisitos clave:
- DICCIONARIO para almacenar libros disponibles: {ISBN: Libro}
- CONJUNTO para asegurar IDs únicos de usuarios
- LISTAS en Usuario para libros prestados
"""

from libro import Libro
from usuario import Usuario


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre.strip() if nombre else "Biblioteca"

        # Libros disponibles (diccionario requerido): ISBN -> Libro
        self.libros_disponibles: dict[str, Libro] = {}

        # Libros prestados (para controlar disponibilidad y dueño del préstamo)
        self.libros_prestados: dict[str, str] = {}  # ISBN -> user_id

        # Usuarios registrados
        self.usuarios: dict[str, Usuario] = {}      # user_id -> Usuario

        # Conjunto requerido para IDs únicos
        self.ids_usuarios: set[str] = set()

        # Historial simple (lista) de préstamos/devoluciones (alineado al objetivo del sistema)
        self.historial: list[str] = []

    # ---------------------------
    # Libros
    # ---------------------------
    def anadir_libro(self, libro: Libro) -> tuple[bool, str]:
        isbn = libro.isbn

        if isbn in self.libros_disponibles or isbn in self.libros_prestados:
            return False, f"Ya existe un libro con ISBN {isbn} en el sistema."

        self.libros_disponibles[isbn] = libro
        return True, f"Libro añadido: {libro}"

    def quitar_libro(self, isbn: str) -> tuple[bool, str]:
        isbn = isbn.strip()
        if isbn in self.libros_prestados:
            return False, f"No se puede quitar. El libro con ISBN {isbn} está prestado."

        if isbn not in self.libros_disponibles:
            return False, f"No existe un libro disponible con ISBN {isbn}."

        libro = self.libros_disponibles.pop(isbn)
        return True, f"Libro quitado: {libro}"

    # ---------------------------
    # Usuarios
    # ---------------------------
    def registrar_usuario(self, usuario: Usuario) -> tuple[bool, str]:
        user_id = usuario.user_id

        # Conjunto requerido: unicidad garantizada
        if user_id in self.ids_usuarios:
            return False, f"El ID {user_id} ya está registrado."

        self.ids_usuarios.add(user_id)
        self.usuarios[user_id] = usuario
        return True, f"Usuario registrado: {usuario}"

    def dar_de_baja_usuario(self, user_id: str) -> tuple[bool, str]:
        user_id = user_id.strip()
        if user_id not in self.ids_usuarios or user_id not in self.usuarios:
            return False, f"No existe un usuario con ID {user_id}."

        usuario = self.usuarios[user_id]
        if usuario.tiene_prestamos():
            return False, "No se puede dar de baja: el usuario tiene libros prestados."

        # Quitar de diccionario y del conjunto
        self.usuarios.pop(user_id)
        self.ids_usuarios.remove(user_id)
        return True, f"Usuario dado de baja: {usuario}"

    # ---------------------------
    # Préstamos
    # ---------------------------
    def prestar_libro(self, user_id: str, isbn: str) -> tuple[bool, str]:
        user_id = user_id.strip()
        isbn = isbn.strip()

        if user_id not in self.usuarios:
            return False, f"Usuario no registrado (ID: {user_id})."

        if isbn not in self.libros_disponibles:
            if isbn in self.libros_prestados:
                duenio = self.libros_prestados[isbn]
                return False, f"El libro ISBN {isbn} ya está prestado a ID {duenio}."
            return False, f"No existe un libro disponible con ISBN {isbn}."

        usuario = self.usuarios[user_id]
        libro = self.libros_disponibles.pop(isbn)

        usuario.prestar_isbn(isbn)
        self.libros_prestados[isbn] = user_id

        self.historial.append(f"PRESTAMO | user_id={user_id} | isbn={isbn}")
        return True, f"Préstamo realizado: {libro} -> {usuario}"

    def devolver_libro(self, user_id: str, isbn: str) -> tuple[bool, str]:
        user_id = user_id.strip()
        isbn = isbn.strip()

        if user_id not in self.usuarios:
            return False, f"Usuario no registrado (ID: {user_id})."

        if isbn not in self.libros_prestados:
            return False, f"El libro ISBN {isbn} no consta como prestado."

        if self.libros_prestados[isbn] != user_id:
            return False, f"El libro ISBN {isbn} no está prestado a ese usuario."

        usuario = self.usuarios[user_id]
        ok = usuario.devolver_isbn(isbn)
        if not ok:
            return False, "El usuario no tenía registrado ese ISBN en su lista de prestados."

        # Recuperar el objeto Libro: estaba fuera de disponibles; lo reconstruimos desde catálogo mínimo
        # Para mantener simpleza, pedimos el libro desde "libros_disponibles"? No está. Entonces:
        # Guardamos el Libro temporalmente al prestar? Mejor: lo guardamos en un catálogo total.
        # Solución directa sin complicar: almacenamos el Libro en disponibles antes de prestarlo (pero ya lo sacamos).
        # Por eso, guardamos el Libro "real" en una estructura interna segura:

        # --- Ajuste: mantener catálogo total (sin romper requisitos) ---
        # Si ya existe _catalogo_total lo usamos; si no, lo creamos al vuelo.
        if not hasattr(self, "_catalogo_total"):
            self._catalogo_total = {}

        # Asegurar que esté registrado el libro en catálogo total
        # (En anadir_libro lo registramos si existe este atributo)
        libro = self._catalogo_total.get(isbn)
        if libro is None:
            return False, "Error interno: no se encontró el libro en el catálogo total."

        # Mover a disponibles nuevamente
        self.libros_disponibles[isbn] = libro
        self.libros_prestados.pop(isbn)

        self.historial.append(f"DEVOLUCION | user_id={user_id} | isbn={isbn}")
        return True, f"Devolución realizada: {libro} <- {usuario}"

    # ---------------------------
    # Búsquedas
    # ---------------------------
    def _todos_los_libros(self) -> list[Libro]:
        # Devuelve todos los libros (disponibles + prestados) como lista
        if not hasattr(self, "_catalogo_total"):
            self._catalogo_total = {}

        # Si el catálogo total está vacío, lo construimos con lo que haya (caso inicial)
        if not self._catalogo_total:
            for isbn, libro in self.libros_disponibles.items():
                self._catalogo_total[isbn] = libro

        return list(self._catalogo_total.values())

    def buscar_por_titulo(self, titulo: str) -> list[Libro]:
        titulo = (titulo or "").casefold().strip()
        return [l for l in self._todos_los_libros() if titulo in l.titulo.casefold()]

    def buscar_por_autor(self, autor: str) -> list[Libro]:
        autor = (autor or "").casefold().strip()
        return [l for l in self._todos_los_libros() if autor in l.autor.casefold()]

    def buscar_por_categoria(self, categoria: str) -> list[Libro]:
        categoria = (categoria or "").casefold().strip()
        return [l for l in self._todos_los_libros() if categoria in l.categoria.casefold()]

    # ---------------------------
    # Listar libros prestados
    # ---------------------------
    def listar_libros_prestados_de_usuario(self, user_id: str) -> tuple[bool, str, list[Libro]]:
        user_id = user_id.strip()
        if user_id not in self.usuarios:
            return False, "Usuario no registrado.", []

        usuario = self.usuarios[user_id]
        if not hasattr(self, "_catalogo_total"):
            self._catalogo_total = {}

        libros = []
        for isbn in usuario.libros_prestados:
            libro = self._catalogo_total.get(isbn)
            if libro is not None:
                libros.append(libro)

        return True, f"Libros prestados a {usuario}:", libros

    # ---------------------------
    # Soporte: mantener catálogo total (sin romper requisitos)
    # ---------------------------
    def registrar_en_catalogo_total(self, libro: Libro) -> None:
        if not hasattr(self, "_catalogo_total"):
            self._catalogo_total = {}
        self._catalogo_total[libro.isbn] = libro