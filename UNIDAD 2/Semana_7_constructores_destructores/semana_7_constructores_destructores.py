class ArchivoSimulado:
    """
    Clase que demuestra el uso de:
    - Constructor (__init__): se ejecuta automáticamente al crear el objeto.
    - Destructor (__del__): se ejecuta cuando el objeto va a eliminarse.
    """

    def __init__(self, nombre_archivo):
        # Constructor: inicializa atributos y deja el objeto listo para usarse.
        # Se activa cuando se crea una instancia: objeto = ArchivoSimulado("datos.txt")
        self.nombre_archivo = nombre_archivo
        self.abierto = True
        print(f"✅ Constructor: Se abrió el recurso '{self.nombre_archivo}'")

    def usar_recurso(self):
        # Método normal para simular que el recurso se está utilizando.
        if self.abierto:
            print(f"📄 Usando el recurso '{self.nombre_archivo}'...")
        else:
            print(f"⚠️ No se puede usar '{self.nombre_archivo}' porque está cerrado.")

    def cerrar(self):
        # Método para simular cierre manual del recurso (buena práctica).
        if self.abierto:
            self.abierto = False
            print(f"🔒 Recurso '{self.nombre_archivo}' cerrado manualmente.")

    def __del__(self):
        # Destructor: se activa cuando el objeto se elimina o el programa finaliza.
        # Se usa para limpieza/cierre de recursos si es aplicable.
        if self.abierto:
            print(f"🧹 Destructor: Cerrando automáticamente '{self.nombre_archivo}' antes de eliminar el objeto.")
            self.abierto = False
        else:
            print(f"🧹 Destructor: El objeto de '{self.nombre_archivo}' se elimina (ya estaba cerrado).")


def main():
    # Crear objeto (aquí se ejecuta el constructor __init__)
    recurso = ArchivoSimulado("reporte_semana_7.txt")

    # Usar el recurso
    recurso.usar_recurso()

    # Cierre manual (opcional, pero muestra buenas prácticas)
    recurso.cerrar()

    # Eliminar el objeto para forzar la llamada al destructor en este ejemplo
    del recurso

    print("✅ Fin del programa.")


if __name__ == "__main__":
    main()
