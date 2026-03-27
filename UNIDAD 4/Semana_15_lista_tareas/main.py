import tkinter as tk
from tkinter import messagebox


class ListaTareasApp:
    def __init__(self, root):
        # Configuración principal de la ventana
        self.root = root
        self.root.title("Lista de Tareas - Semana 15")
        self.root.geometry("520x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f8")

        # Lista interna donde se almacenan las tareas y su estado
        self.tareas = []

        # Título principal
        self.titulo = tk.Label(
            self.root,
            text="Aplicación GUI de Lista de Tareas",
            font=("Arial", 16, "bold"),
            bg="#f4f6f8"
        )
        self.titulo.pack(pady=15)

        # Frame para la entrada de texto
        self.frame_entrada = tk.Frame(self.root, bg="#f4f6f8")
        self.frame_entrada.pack(pady=5)

        self.lbl_tarea = tk.Label(
            self.frame_entrada,
            text="Nueva tarea:",
            font=("Arial", 11),
            bg="#f4f6f8"
        )
        self.lbl_tarea.grid(row=0, column=0, padx=5, pady=5)

        # Campo Entry para escribir nuevas tareas
        self.entry_tarea = tk.Entry(self.frame_entrada, width=35, font=("Arial", 11))
        self.entry_tarea.grid(row=0, column=1, padx=5, pady=5)

        # Evento Enter para añadir una tarea directamente desde el teclado
        self.entry_tarea.bind("<Return>", self.agregar_tarea)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.root, bg="#f4f6f8")
        self.frame_botones.pack(pady=10)

        # Botón para añadir tarea
        self.btn_agregar = tk.Button(
            self.frame_botones,
            text="Añadir Tarea",
            width=18,
            command=self.agregar_tarea
        )
        self.btn_agregar.grid(row=0, column=0, padx=5, pady=5)

        # Botón para marcar tarea como completada
        self.btn_completar = tk.Button(
            self.frame_botones,
            text="Marcar como Completada",
            width=22,
            command=self.marcar_completada
        )
        self.btn_completar.grid(row=0, column=1, padx=5, pady=5)

        # Botón para eliminar tarea
        self.btn_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar Tarea",
            width=18,
            command=self.eliminar_tarea
        )
        self.btn_eliminar.grid(row=0, column=2, padx=5, pady=5)

        # Frame para la lista de tareas
        self.frame_lista = tk.Frame(self.root, bg="#f4f6f8")
        self.frame_lista.pack(pady=10, fill="both", expand=True)

        # Barra de desplazamiento para la lista
        self.scrollbar = tk.Scrollbar(self.frame_lista)
        self.scrollbar.pack(side="right", fill="y")

        # Listbox para mostrar las tareas actuales
        self.listbox_tareas = tk.Listbox(
            self.frame_lista,
            width=60,
            height=12,
            font=("Arial", 11),
            yscrollcommand=self.scrollbar.set,
            selectbackground="#cfe2ff",
            activestyle="none"
        )
        self.listbox_tareas.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.listbox_tareas.yview)

        # Evento opcional: doble clic para marcar una tarea como completada
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada)

        # Colocar el cursor dentro del Entry al abrir la app
        self.entry_tarea.focus()

    def agregar_tarea(self, event=None):
        """
        Agrega una nueva tarea a la lista.
        Este método puede ejecutarse desde:
        - el botón 'Añadir Tarea'
        - la tecla Enter en el Entry
        """
        texto_tarea = self.entry_tarea.get().strip()

        if texto_tarea == "":
            messagebox.showwarning("Campo vacío", "Debe escribir una tarea.")
            return

        # Se guarda cada tarea con su texto y estado de completada
        nueva_tarea = {
            "texto": texto_tarea,
            "completada": False
        }
        self.tareas.append(nueva_tarea)

        # Se refresca la lista visual
        self.actualizar_lista()

        # Limpiar el campo de entrada para seguir escribiendo
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus()

    def marcar_completada(self, event=None):
        """
        Marca la tarea seleccionada como completada.
        Cambia su estado visual en la lista.
        """
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccione una tarea para marcarla como completada.")
            return

        indice = seleccion[0]
        self.tareas[indice]["completada"] = True
        self.actualizar_lista()

        # Mantener seleccionada la misma tarea
        self.listbox_tareas.selection_set(indice)

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista.
        """
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccione una tarea para eliminarla.")
            return

        indice = seleccion[0]
        del self.tareas[indice]
        self.actualizar_lista()

    def actualizar_lista(self):
        """
        Limpia y vuelve a dibujar la lista de tareas.
        Las tareas completadas cambian visualmente.
        """
        self.listbox_tareas.delete(0, tk.END)

        for i, tarea in enumerate(self.tareas):
            if tarea["completada"]:
                texto_mostrado = f"✔ {tarea['texto']}"
            else:
                texto_mostrado = f"○ {tarea['texto']}"

            self.listbox_tareas.insert(tk.END, texto_mostrado)

            # Cambio visual para tareas completadas
            if tarea["completada"]:
                self.listbox_tareas.itemconfig(i, fg="green")
            else:
                self.listbox_tareas.itemconfig(i, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()