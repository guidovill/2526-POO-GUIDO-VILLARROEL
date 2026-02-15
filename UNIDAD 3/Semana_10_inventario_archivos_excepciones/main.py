from inventario import Inventario
from producto import Producto


def leer_entero(msg: str) -> int:
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número entero.")


def leer_flotante(msg: str) -> float:
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("❌ Entrada inválida. Ingrese un número decimal válido.")


def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS (SEMANA 10) ===")
    print("1) Añadir producto")
    print("2) Eliminar producto por ID")
    print("3) Actualizar cantidad/precio por ID")
    print("4) Buscar producto(s) por nombre")
    print("5) Mostrar todos los productos")
    print("0) Salir")


def main():
    inventario = Inventario()
    inicio = inventario.get_mensaje_inicio()
    if inicio:
        print(inicio)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            producto_id = input("ID (único): ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = leer_entero("Cantidad: ")
            precio = leer_flotante("Precio: ")

            if not producto_id or not nombre:
                print("❌ ID y Nombre no pueden estar vacíos.")
                continue
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa.")
                continue
            if precio < 0:
                print("❌ El precio no puede ser negativo.")
                continue

            p = Producto(producto_id, nombre, cantidad, precio)
            ok, msg = inventario.anadir_producto(p)
            print(msg)

        elif opcion == "2":
            producto_id = input("Ingrese el ID a eliminar: ").strip()
            ok, msg = inventario.eliminar_producto_por_id(producto_id)
            print(msg)

        elif opcion == "3":
            producto_id = input("Ingrese el ID a actualizar: ").strip()

            if not inventario.id_existe(producto_id):
                print("⚠️ No se encontró un producto con ese ID.")
                continue

            print("Deje en blanco si no desea actualizar un campo.")
            txt_cantidad = input("Nueva cantidad: ").strip()
            txt_precio = input("Nuevo precio: ").strip()

            nueva_cantidad = None
            nuevo_precio = None

            if txt_cantidad != "":
                try:
                    nueva_cantidad = int(txt_cantidad)
                    if nueva_cantidad < 0:
                        print("❌ La cantidad no puede ser negativa.")
                        continue
                except ValueError:
                    print("❌ Cantidad inválida.")
                    continue

            if txt_precio != "":
                try:
                    nuevo_precio = float(txt_precio)
                    if nuevo_precio < 0:
                        print("❌ El precio no puede ser negativo.")
                        continue
                except ValueError:
                    print("❌ Precio inválido.")
                    continue

            if nueva_cantidad is None and nuevo_precio is None:
                print("⚠️ No se ingresó ningún cambio.")
                continue

            ok, msg = inventario.actualizar_producto_por_id(producto_id, nueva_cantidad, nuevo_precio)
            print(msg)

        elif opcion == "4":
            texto = input("Ingrese nombre o parte del nombre: ").strip()
            resultados = inventario.buscar_por_nombre(texto)
            if not resultados:
                print("No se encontraron coincidencias.")
            else:
                print("\n--- Resultados ---")
                for p in resultados:
                    print(p)

        elif opcion == "5":
            productos = inventario.obtener_todos()
            if not productos:
                print("Inventario vacío.")
            else:
                print("\n--- Inventario ---")
                for p in productos:
                    print(p)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()