import tkinter as tk
from tkinter import messagebox


class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas - Semana 16")
        self.root.geometry("620x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f8")

        # Lista interna de tareas
        # Cada tarea se guarda como diccionario: {"texto": str, "completada": bool}
        self.tareas = []

        # Título
        self.lbl_titulo = tk.Label(
            self.root,
            text="Aplicación GUI para Gestión de Tareas",
            font=("Arial", 16, "bold"),
            bg="#f4f6f8",
            fg="#1f2937"
        )
        self.lbl_titulo.pack(pady=(15, 10))

        # Marco de entrada
        self.frame_entrada = tk.Frame(self.root, bg="#f4f6f8")
        self.frame_entrada.pack(pady=10, padx=20, fill="x")

        self.lbl_entrada = tk.Label(
            self.frame_entrada,
            text="Nueva tarea:",
            font=("Arial", 11),
            bg="#f4f6f8",
            fg="#111827"
        )
        self.lbl_entrada.pack(anchor="w")

        self.entry_tarea = tk.Entry(
            self.frame_entrada,
            font=("Arial", 12),
            width=40
        )
        self.entry_tarea.pack(side="left", pady=8, padx=(0, 10), fill="x", expand=True)
        self.entry_tarea.focus_set()

        self.btn_agregar = tk.Button(
            self.frame_entrada,
            text="Añadir tarea",
            font=("Arial", 11, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            command=self.agregar_tarea
        )
        self.btn_agregar.pack(side="right")

        # Marco de lista
        self.frame_lista = tk.Frame(self.root, bg="#f4f6f8")
        self.frame_lista.pack(padx=20, pady=10, fill="both", expand=True)

        self.lbl_lista = tk.Label(
            self.frame_lista,
            text="Lista de tareas:",
            font=("Arial", 11),
            bg="#f4f6f8",
            fg="#111827"
        )
        self.lbl_lista.pack(anchor="w")

        self.listbox_tareas = tk.Listbox(
            self.frame_lista,
            font=("Arial", 12),
            height=14,
            selectbackground="#93c5fd",
            activestyle="none"
        )
        self.listbox_tareas.pack(side="left", fill="both", expand=True, pady=8)

        self.scrollbar = tk.Scrollbar(self.frame_lista, orient="vertical")
        self.scrollbar.config(command=self.listbox_tareas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox_tareas.config(yscrollcommand=self.scrollbar.set)

        # Botones de acción
        self.frame_botones = tk.Frame(self.root, bg="#f4f6f8")
        self.frame_botones.pack(pady=10)

        self.btn_completar = tk.Button(
            self.frame_botones,
            text="Marcar como completada",
            font=("Arial", 11, "bold"),
            bg="#16a34a",
            fg="white",
            activebackground="#15803d",
            activeforeground="white",
            width=22,
            command=self.marcar_completada
        )
        self.btn_completar.grid(row=0, column=0, padx=10)

        self.btn_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar tarea",
            font=("Arial", 11, "bold"),
            bg="#dc2626",
            fg="white",
            activebackground="#b91c1c",
            activeforeground="white",
            width=16,
            command=self.eliminar_tarea
        )
        self.btn_eliminar.grid(row=0, column=1, padx=10)

        # Etiqueta de atajos
        self.lbl_atajos = tk.Label(
            self.root,
            text="Atajos: Enter = añadir | C = completar | D / Delete = eliminar | Escape = cerrar",
            font=("Arial", 10),
            bg="#f4f6f8",
            fg="#4b5563"
        )
        self.lbl_atajos.pack(pady=(5, 15))

        # Vinculación de eventos de teclado
        self.root.bind("<Return>", self.evento_agregar_tarea)
        self.root.bind("<Escape>", self.cerrar_aplicacion)
        self.root.bind("<Delete>", self.evento_eliminar_tarea)
        self.root.bind("<d>", self.evento_eliminar_tarea)
        self.root.bind("<D>", self.evento_eliminar_tarea)
        self.root.bind("<c>", self.evento_completar_tarea)
        self.root.bind("<C>", self.evento_completar_tarea)

    def agregar_tarea(self):
        texto = self.entry_tarea.get().strip()

        if not texto:
            messagebox.showwarning("Campo vacío", "Debe escribir una tarea antes de añadirla.")
            return

        self.tareas.append({"texto": texto, "completada": False})
        self.entry_tarea.delete(0, tk.END)
        self.actualizar_lista()

    def marcar_completada(self):
        indice = self.obtener_indice_seleccionado()
        if indice is None:
            return

        if self.tareas[indice]["completada"]:
            messagebox.showinfo("Información", "La tarea seleccionada ya está completada.")
            return

        self.tareas[indice]["completada"] = True
        self.actualizar_lista()
        self.listbox_tareas.selection_set(indice)

    def eliminar_tarea(self):
        indice = self.obtener_indice_seleccionado()
        if indice is None:
            return

        del self.tareas[indice]
        self.actualizar_lista()

    def obtener_indice_seleccionado(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Debe seleccionar una tarea de la lista.")
            return None
        return seleccion[0]

    def actualizar_lista(self):
        self.listbox_tareas.delete(0, tk.END)

        for indice, tarea in enumerate(self.tareas):
            if tarea["completada"]:
                texto_mostrado = f"✔ {tarea['texto']}"
            else:
                texto_mostrado = f"• {tarea['texto']}"

            self.listbox_tareas.insert(tk.END, texto_mostrado)

            if tarea["completada"]:
                self.listbox_tareas.itemconfig(indice, fg="gray")
            else:
                self.listbox_tareas.itemconfig(indice, fg="black")

    def evento_agregar_tarea(self, event):
        self.agregar_tarea()

    def evento_completar_tarea(self, event):
        self.marcar_completada()

    def evento_eliminar_tarea(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event=None):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()