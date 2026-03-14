import tkinter as tk
from tkinter import ttk, messagebox


class BibliotecaDigitalGUI:
    """
    Aplicación GUI básica desarrollada con Tkinter.
    Permite agregar libros a una tabla y limpiar los datos ingresados
    o el registro seleccionado, cumpliendo con la tarea de la Semana 13.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca Digital GUI - Semana 13")
        self.root.geometry("780x520")
        self.root.minsize(780, 520)

        # Contador para asignar un identificador simple a cada registro.
        self.contador_id = 1

        # Variables de control para los campos de texto.
        self.titulo_var = tk.StringVar()
        self.autor_var = tk.StringVar()

        # Construcción de la interfaz.
        self.crear_interfaz()
        self.configurar_eventos()

    def crear_interfaz(self):
        """Crea y organiza todos los componentes visuales de la ventana."""
        contenedor = ttk.Frame(self.root, padding=15)
        contenedor.pack(fill="both", expand=True)

        # Título principal de la aplicación.
        titulo_principal = ttk.Label(
            contenedor,
            text="Biblioteca Digital GUI",
            font=("Segoe UI", 18, "bold")
        )
        titulo_principal.pack(anchor="center", pady=(0, 5))

        # Texto descriptivo para orientar al usuario.
        descripcion = ttk.Label(
            contenedor,
            text="Ingrese un libro y su autor. Luego presione 'Agregar' para mostrarlo en la tabla.",
            font=("Segoe UI", 10)
        )
        descripcion.pack(anchor="center", pady=(0, 15))

        # Marco para los campos de entrada.
        marco_formulario = ttk.LabelFrame(contenedor, text="Ingreso de datos", padding=15)
        marco_formulario.pack(fill="x", pady=(0, 12))

        # Label y campo de texto para el título del libro.
        lbl_titulo = ttk.Label(marco_formulario, text="Título del libro:")
        lbl_titulo.grid(row=0, column=0, padx=(0, 10), pady=8, sticky="w")

        self.entry_titulo = ttk.Entry(marco_formulario, textvariable=self.titulo_var, width=40)
        self.entry_titulo.grid(row=0, column=1, padx=(0, 15), pady=8, sticky="ew")

        # Label y campo de texto para el autor.
        lbl_autor = ttk.Label(marco_formulario, text="Autor:")
        lbl_autor.grid(row=1, column=0, padx=(0, 10), pady=8, sticky="w")

        self.entry_autor = ttk.Entry(marco_formulario, textvariable=self.autor_var, width=40)
        self.entry_autor.grid(row=1, column=1, padx=(0, 15), pady=8, sticky="ew")

        # Permite que el formulario se adapte horizontalmente.
        marco_formulario.columnconfigure(1, weight=1)

        # Marco para los botones.
        marco_botones = ttk.Frame(contenedor)
        marco_botones.pack(fill="x", pady=(0, 12))

        # Botón para agregar registros a la tabla.
        btn_agregar = ttk.Button(marco_botones, text="Agregar", command=self.agregar_libro)
        btn_agregar.pack(side="left", padx=(0, 10))

        # Botón para limpiar los campos y eliminar el elemento seleccionado si existe.
        btn_limpiar = ttk.Button(marco_botones, text="Limpiar", command=self.limpiar_datos)
        btn_limpiar.pack(side="left", padx=(0, 10))

        # Botón extra para cerrar la aplicación.
        btn_salir = ttk.Button(marco_botones, text="Salir", command=self.root.destroy)
        btn_salir.pack(side="right")

        # Marco para la tabla de datos.
        marco_tabla = ttk.LabelFrame(contenedor, text="Libros registrados", padding=10)
        marco_tabla.pack(fill="both", expand=True)

        columnas = ("ID", "Título", "Autor")
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas, show="headings", height=12)

        # Encabezados de la tabla.
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Título", text="Título")
        self.tabla.heading("Autor", text="Autor")

        # Tamaño de las columnas.
        self.tabla.column("ID", width=70, anchor="center")
        self.tabla.column("Título", width=340, anchor="w")
        self.tabla.column("Autor", width=250, anchor="w")

        # Barra de desplazamiento vertical para la tabla.
        scrollbar = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Etiqueta inferior para mostrar cantidad total de registros.
        self.lbl_total = ttk.Label(contenedor, text="Total de registros: 0", font=("Segoe UI", 10, "bold"))
        self.lbl_total.pack(anchor="e", pady=(10, 0))

        # Coloca el cursor en el primer campo al iniciar la app.
        self.entry_titulo.focus()

    def configurar_eventos(self):
        """
        Configura eventos adicionales de teclado y selección.
        Enter agrega un registro.
        Escape limpia los datos.
        Seleccionar una fila carga sus datos en los campos.
        """
        self.root.bind("<Return>", self.agregar_desde_teclado)
        self.root.bind("<Escape>", self.limpiar_desde_teclado)
        self.tabla.bind("<<TreeviewSelect>>", self.cargar_registro_seleccionado)

    def agregar_desde_teclado(self, event):
        """Permite agregar un libro usando la tecla Enter."""
        self.agregar_libro()

    def limpiar_desde_teclado(self, event):
        """Permite limpiar usando la tecla Escape."""
        self.limpiar_datos()

    def agregar_libro(self):
        """
        Agrega un nuevo libro a la tabla si los campos tienen información.
        También valida que no existan campos vacíos.
        """
        titulo = self.titulo_var.get().strip()
        autor = self.autor_var.get().strip()

        if not titulo or not autor:
            messagebox.showwarning(
                "Datos incompletos",
                "Debe ingresar el título del libro y el autor."
            )
            return

        # Inserta el nuevo registro en la tabla.
        self.tabla.insert("", "end", values=(self.contador_id, titulo, autor))
        self.contador_id += 1

        # Limpia los campos después de agregar.
        self.titulo_var.set("")
        self.autor_var.set("")

        # Actualiza el total y regresa el foco al primer campo.
        self.actualizar_total()
        self.entry_titulo.focus()

    def limpiar_datos(self):
        """
        Limpia los campos de texto.
        Si hay un registro seleccionado, también lo elimina de la tabla.
        Esto cumple con la consigna de limpiar información ingresada o seleccionada.
        """
        seleccion = self.tabla.selection()

        # Siempre limpia los campos del formulario.
        self.titulo_var.set("")
        self.autor_var.set("")

        # Si el usuario seleccionó un registro, se elimina.
        if seleccion:
            for item in seleccion:
                self.tabla.delete(item)
            self.actualizar_total()

        self.entry_titulo.focus()

    def cargar_registro_seleccionado(self, event):
        """
        Carga en los campos el registro seleccionado en la tabla.
        Esto mejora la interacción del usuario con la interfaz.
        """
        seleccion = self.tabla.selection()
        if not seleccion:
            return

        valores = self.tabla.item(seleccion[0], "values")
        if len(valores) == 3:
            self.titulo_var.set(valores[1])
            self.autor_var.set(valores[2])

    def actualizar_total(self):
        """Actualiza la etiqueta que muestra la cantidad de registros en la tabla."""
        total = len(self.tabla.get_children())
        self.lbl_total.config(text=f"Total de registros: {total}")


def main():
    """Función principal para iniciar la aplicación."""
    root = tk.Tk()
    app = BibliotecaDigitalGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()