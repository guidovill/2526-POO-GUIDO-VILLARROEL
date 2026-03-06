# Semana 12 - Sistema de Gestión de Biblioteca Digital

## Objetivo
Implementar un sistema en Python con Programación Orientada a Objetos para gestionar una biblioteca digital:
- Libros disponibles, categorías, usuarios y préstamos.
- Uso obligatorio de colecciones para mejorar rendimiento.

## Estructuras usadas (requisito)
- **Tupla**: (autor, título) dentro de `Libro`.
- **Lista**: libros prestados por usuario (lista de ISBNs).
- **Diccionario**: libros disponibles por ISBN.
- **Conjunto (set)**: IDs únicos de usuarios.

## Archivos
- `libro.py`: clase Libro
- `usuario.py`: clase Usuario
- `biblioteca.py`: clase Biblioteca (gestiona todo)
- `main.py`: pruebas (crear objetos y ejecutar operaciones)

## Ejecución
Desde la carpeta `Semana_12_biblioteca_digital_colecciones`:

```bash
python main.py