import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitas

class AppVisits(tk.Tk):
   def __init__(self, servicio):
        super().__init__(self, self.servicios)

        # Inyección de dependencias
        self.servicio = self.servicios

        self.title("Registro de Visitantes")
        self.geometry("500x500")

        self.crear_ineterfaz()

    def crear_interfaz(self):
        # ===== FORMULARIO =====
        tk.Label(self, text="Cédula").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(self)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(self, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(self, text="Motivo").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(self)
        self.entry_motivo.grid(row=2, column=1)

        # ===== BOTONES =====
        tk.Button(self, text="Registrar", command=self.registrar).grid(row=3, column=0)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(self, text="Limpiar", command=self.limpiar).grid(row=3, column=2)

        # ===== TABLA =====
        self.tree = ttk.Treeview(self, columns=("Cedula", "Nombre", "Motivo"), show="headings")

        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")

        self.tree.grid(row=4, column=0, columnspan=3)

    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            # Crear visitante usando el servicio
            from modelos.visitante import Visitante
            visitante = Visitante(cedula, nombre, motivo)

            self.servicio.crear(visitante)

            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showerror("Error", "Seleccione un registro")
            return

        item = self.tree.item(seleccion)
        cedula = item["values"][0]

        self.servicio.eliminar(cedula)
        self.actualizar_tabla()

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for v in self.servicio.listar_todo():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))