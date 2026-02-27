# Semana 11 - Sistema Avanzado de Gestión de Inventario

## Colecciones usadas
- Diccionario: se almacena el inventario como {id: Producto} para búsqueda rápida por ID.
- Lista: se usa para mostrar todos los productos y los resultados de búsqueda (ordenados).
- Conjunto (set): se usa para guardar IDs encontrados en la búsqueda por nombre sin duplicados.
- Tupla: cada producto se representa como (id, nombre, cantidad, precio) para mostrar y serializar.

## Archivos (persistencia)
- inventario.txt: guarda el inventario en formato JSON.
- Serialización: el diccionario del inventario se convierte a datos guardables (tuplas convertidas a listas).
- Deserialización: al iniciar, se lee el archivo y se reconstruye {id: Producto}.