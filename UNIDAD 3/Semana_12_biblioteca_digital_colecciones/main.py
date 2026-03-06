from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


def imprimir_resultado(ok: bool, msg: str):
    estado = "✅" if ok else "❌"
    print(f"{estado} {msg}")


def main():
    print("=== SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL (Semana 12) ===\n")

    biblioteca = Biblioteca("Biblioteca Digital UEA")

    # Crear libros (autor y título en tupla dentro de Libro)
    libros = [
        Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "ISBN-001"),
        Libro("Clean Code", "Robert C. Martin", "Programación", "ISBN-002"),
        Libro("El principito", "Antoine de Saint-Exupéry", "Fábula", "ISBN-003"),
        Libro("Python Crash Course", "Eric Matthes", "Programación", "ISBN-004"),
    ]

    # Añadir libros a la biblioteca
    print(">> Añadiendo libros al catálogo:")
    for libro in libros:
        biblioteca.registrar_en_catalogo_total(libro)  # soporte interno del catálogo total
        ok, msg = biblioteca.anadir_libro(libro)
        imprimir_resultado(ok, msg)
    print()

    # Registrar usuarios (IDs únicos controlados por set)
    print(">> Registrando usuarios:")
    u1 = Usuario("Guido Villarroel", "U001")
    u2 = Usuario("Ariel Reinoso", "U002")

    ok, msg = biblioteca.registrar_usuario(u1)
    imprimir_resultado(ok, msg)

    ok, msg = biblioteca.registrar_usuario(u2)
    imprimir_resultado(ok, msg)

    # Intento duplicado para demostrar unicidad
    u3 = Usuario("Usuario Duplicado", "U002")
    ok, msg = biblioteca.registrar_usuario(u3)
    imprimir_resultado(ok, msg)
    print()

    # Préstamos
    print(">> Préstamos:")
    ok, msg = biblioteca.prestar_libro("U001", "ISBN-002")
    imprimir_resultado(ok, msg)

    ok, msg = biblioteca.prestar_libro("U001", "ISBN-003")
    imprimir_resultado(ok, msg)

    # Intento de prestar un libro ya prestado
    ok, msg = biblioteca.prestar_libro("U002", "ISBN-002")
    imprimir_resultado(ok, msg)
    print()

    # Listar prestados de un usuario
    print(">> Listar libros prestados del usuario U001:")
    ok, msg, lista = biblioteca.listar_libros_prestados_de_usuario("U001")
    imprimir_resultado(ok, msg)
    for libro in lista:
        print("   -", libro)
    print()

    # Búsquedas
    print(">> Búsquedas:")
    print("Buscar por categoría 'Programación':")
    for libro in biblioteca.buscar_por_categoria("Programación"):
        print("   -", libro)

    print("\nBuscar por autor 'García':")
    for libro in biblioteca.buscar_por_autor("García"):
        print("   -", libro)

    print("\nBuscar por título 'principito':")
    for libro in biblioteca.buscar_por_titulo("principito"):
        print("   -", libro)
    print()

    # Devolución
    print(">> Devolución:")
    ok, msg = biblioteca.devolver_libro("U001", "ISBN-002")
    imprimir_resultado(ok, msg)

    # Intento de devolver algo no prestado a ese usuario
    ok, msg = biblioteca.devolver_libro("U002", "ISBN-003")
    imprimir_resultado(ok, msg)
    print()

    # Dar de baja usuario con libros prestados (debería fallar)
    print(">> Dar de baja usuario:")
    ok, msg = biblioteca.dar_de_baja_usuario("U001")
    imprimir_resultado(ok, msg)

    # Devolver lo pendiente
    ok, msg = biblioteca.devolver_libro("U001", "ISBN-003")
    imprimir_resultado(ok, msg)

    # Ahora sí dar de baja
    ok, msg = biblioteca.dar_de_baja_usuario("U001")
    imprimir_resultado(ok, msg)
    print()

    # Historial simple
    print(">> Historial de operaciones:")
    for evento in biblioteca.historial:
        print("   -", evento)

    print("\n=== FIN DE PRUEBAS ===")


if __name__ == "__main__":
    main()