import re
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaPersonalApp:
    """
    Aplicación GUI de agenda personal desarrollada con Tkinter.
    Permite agregar, visualizar y eliminar eventos programados.
    """

    def __init__(self, root):
        # Ventana principal
        self.root = root
        self.root.title("Agenda Personal - Semana 14")
        self.root.geometry("800x520")
        self.root.resizable(False, False)

        # Crear toda la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        """
        Crea y organiza todos los componentes de la interfaz
        utilizando Frames para separar visualmente las secciones.
        """

        # =========================
        # Frame superior: título
        # =========================
        frame_titulo = ttk.Frame(self.root, padding=10)
        frame_titulo.pack(fill="x")

        lbl_titulo = ttk.Label(
            frame_titulo,
            text="Agenda Personal",
            font=("Arial", 18, "bold")
        )
        lbl_titulo.pack()

        # =========================
        # Frame central: tabla
        # =========================
        frame_tabla = ttk.LabelFrame(self.root, text="Eventos Programados", padding=10)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Definición de columnas del TreeView
        columnas = ("fecha", "hora", "descripcion")

        self.tree = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=12
        )

        # Encabezados
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")

        # Tamaño de columnas
        self.tree.column("fecha", width=130, anchor="center")
        self.tree.column("hora", width=100, anchor="center")
        self.tree.column("descripcion", width=500, anchor="w")

        # Barra de desplazamiento vertical
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # =========================
        # Frame inferior: entradas
        # =========================
        frame_entrada = ttk.LabelFrame(self.root, text="Ingreso de Datos", padding=10)
        frame_entrada.pack(fill="x", padx=10, pady=5)

        # Label y DatePicker para fecha
        lbl_fecha = ttk.Label(frame_entrada, text="Fecha:")
        lbl_fecha.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.date_picker = DateEntry(
            frame_entrada,
            width=18,
            date_pattern="yyyy-mm-dd"
        )
        self.date_picker.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Label y Entry para hora
        lbl_hora = ttk.Label(frame_entrada, text="Hora (HH:MM):")
        lbl_hora.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.entry_hora = ttk.Entry(frame_entrada, width=20)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Label y Entry para descripción
        lbl_descripcion = ttk.Label(frame_entrada, text="Descripción:")
        lbl_descripcion.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.entry_descripcion = ttk.Entry(frame_entrada, width=70)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

        # =========================
        # Frame final: botones
        # =========================
        frame_botones = ttk.Frame(self.root, padding=10)
        frame_botones.pack(fill="x")

        btn_agregar = ttk.Button(
            frame_botones,
            text="Agregar Evento",
            command=self.agregar_evento
        )
        btn_agregar.pack(side="left", padx=5)

        btn_eliminar = ttk.Button(
            frame_botones,
            text="Eliminar Evento Seleccionado",
            command=self.eliminar_evento
        )
        btn_eliminar.pack(side="left", padx=5)

        btn_salir = ttk.Button(
            frame_botones,
            text="Salir",
            command=self.salir_aplicacion
        )
        btn_salir.pack(side="right", padx=5)

    def hora_valida(self, hora):
        """
        Verifica si la hora ingresada tiene el formato HH:MM
        y se encuentra dentro de un rango válido.
        """
        patron = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        return re.match(patron, hora) is not None

    def agregar_evento(self):
        """
        Agrega un nuevo evento al TreeView luego de validar
        que todos los campos estén completos.
        """
        fecha = self.date_picker.get().strip()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()

        # Validar campos vacíos
        if not fecha or not hora or not descripcion:
            messagebox.showwarning(
                "Campos incompletos",
                "Por favor, complete todos los campos."
            )
            return

        # Validar formato de hora
        if not self.hora_valida(hora):
            messagebox.showerror(
                "Hora inválida",
                "Ingrese la hora en formato HH:MM, por ejemplo 08:30 o 14:45."
            )
            return

        # Insertar el evento en la tabla
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

        # Limpiar campos después de agregar
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_hora.focus()

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        """
        Elimina el evento seleccionado del TreeView.
        Incluye confirmación antes de borrar.
        """
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Sin selección",
                "Seleccione un evento para eliminar."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de eliminar el evento seleccionado?"
        )

        if confirmar:
            for item in seleccionado:
                self.tree.delete(item)

            messagebox.showinfo("Eliminado", "Evento eliminado correctamente.")

    def salir_aplicacion(self):
        """
        Cierra la aplicación.
        """
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonalApp(root)
    root.mainloop()