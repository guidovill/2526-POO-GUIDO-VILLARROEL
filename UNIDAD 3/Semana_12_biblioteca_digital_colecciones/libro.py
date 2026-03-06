"""
Clase Libro
- Guarda (autor, título) en una TUPLA porque no deben cambiar una vez creado el libro.
- ISBN identifica de forma única a cada libro.
"""

class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        if not titulo or not autor or not categoria or not isbn:
            raise ValueError("Los campos título, autor, categoría e ISBN son obligatorios.")

        # Tupla inmutable: (autor, título)
        self._autor_titulo = (autor.strip(), titulo.strip())
        self.categoria = categoria.strip()
        self.isbn = isbn.strip()

    @property
    def autor(self) -> str:
        return self._autor_titulo[0]

    @property
    def titulo(self) -> str:
        return self._autor_titulo[1]

    def __str__(self) -> str:
        return f"'{self.titulo}' - {self.autor} | {self.categoria} | ISBN: {self.isbn}"

    def __repr__(self) -> str:
        return f"Libro(titulo={self.titulo!r}, autor={self.autor!r}, categoria={self.categoria!r}, isbn={self.isbn!r})"