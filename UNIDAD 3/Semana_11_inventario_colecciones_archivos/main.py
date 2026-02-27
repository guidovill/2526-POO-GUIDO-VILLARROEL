from inventario import Inventario
from producto import Producto


def leer_no_vacio(msg):
    while True:
        val = input(msg).strip()
        if val:
            return val
        print("Dato obligatorio. Intente de nuevo.")


def leer_int(msg):
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Debe ingresar un número entero.")


def leer_float(msg):
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            print("Debe ingresar un número (ej: 1.25).")


def mostrar_productos(productos):
    if not productos:
        print("No hay productos para mostrar.")
        return

    print("\nID | Nombre | Cantidad | Precio")
    print("-" * 35)
    for p in productos:
        pid, nombre, cant, precio = p.como_tupla()  # tupla
        print(f"{pid} | {nombre} | {cant} | {precio:.2f}")


def main():
    inv = Inventario()  # carga automática desde inventario.txt

    while True:
        print("\nSistema Avanzado de Gestión de Inventario - Semana 11")
        print("1. Añadir producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar y mostrar por nombre")
        print("6. Mostrar todos los productos")
        print("0. Salir")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            try:
                pid = leer_no_vacio("ID: ")
                nombre = leer_no_vacio("Nombre: ")
                cantidad = leer_int("Cantidad: ")
                precio = leer_float("Precio: ")

                prod = Producto(pid, nombre, cantidad, precio)
                ok = inv.anadir_producto(prod)

                if ok:
                    print("Producto añadido correctamente.")
                else:
                    print("Ya existe un producto con ese ID (debe ser único).")

            except ValueError as e:
                print(f"Error: {e}")

        elif op == "2":
            pid = leer_no_vacio("ID a eliminar: ")
            ok = inv.eliminar_producto_por_id(pid)
            if ok:
                print("Producto eliminado correctamente.")
            else:
                print("No existe un producto con ese ID.")

        elif op == "3":
            pid = leer_no_vacio("ID a actualizar cantidad: ")
            cant = leer_int("Nueva cantidad: ")
            try:
                ok = inv.actualizar_cantidad(pid, cant)
                if ok:
                    print("Cantidad actualizada correctamente.")
                else:
                    print("No existe un producto con ese ID.")
            except ValueError as e:
                print(f"Error: {e}")

        elif op == "4":
            pid = leer_no_vacio("ID a actualizar precio: ")
            pre = leer_float("Nuevo precio: ")
            try:
                ok = inv.actualizar_precio(pid, pre)
                if ok:
                    print("Precio actualizado correctamente.")
                else:
                    print("No existe un producto con ese ID.")
            except ValueError as e:
                print(f"Error: {e}")

        elif op == "5":
            texto = leer_no_vacio("Nombre (o parte del nombre): ")
            encontrados = inv.buscar_y_mostrar_por_nombre(texto)
            mostrar_productos(encontrados)

        elif op == "6":
            todos = inv.mostrar_todos()
            mostrar_productos(todos)

        elif op == "0":
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()