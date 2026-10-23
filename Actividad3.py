import tkinter as tk
from tkinter import ttk, messagebox

class GestionEmpleadosGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 8.2 y 8.3 - Gestión de Empleados (Tkinter)")
        self.root.geometry("850x600")
        self.root.resizable(True, True)

        self.fila_seleccionada = None

        # -------------------------------------------------------------------
        # 1. PANEL FORMULARIO (Ejercicio 8.2)
        # -------------------------------------------------------------------
        frame_form = ttk.LabelFrame(self.root, text="Datos del Empleado", padding=(10, 10))
        frame_form.pack(fill="x", padx=10, pady=5)

        # Campo ID
        ttk.Label(frame_form, text="ID / Documento:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.txt_id = ttk.Entry(frame_form, width=25)
        self.txt_id.grid(row=0, column=1, sticky="w", pady=5, padx=5)

        # Campo Nombre
        ttk.Label(frame_form, text="Nombre Completo:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.txt_nombre = ttk.Entry(frame_form, width=25)
        self.txt_nombre.grid(row=1, column=1, sticky="w", pady=5, padx=5)

        # Campo Género (RadioButtons)
        ttk.Label(frame_form, text="Género:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.var_genero = tk.StringVar(value="Masculino")
        frame_genero = ttk.Frame(frame_form)
        frame_genero.grid(row=2, column=1, sticky="w", pady=5, padx=5)
        ttk.Radiobutton(frame_genero, text="Masculino", variable=self.var_genero, value="Masculino").pack(side="left", padx=5)
        ttk.Radiobutton(frame_genero, text="Femenino", variable=self.var_genero, value="Femenino").pack(side="left", padx=5)

        # Campo Departamento (Combobox)
        ttk.Label(frame_form, text="Departamento:").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        self.cb_depto = ttk.Combobox(frame_form, values=["Sistemas", "Recursos Humanos", "Contabilidad", "Ventas"], state="readonly", width=23)
        self.cb_depto.current(0)
        self.cb_depto.grid(row=3, column=1, sticky="w", pady=5, padx=5)

        # Campo Sueldo con Validación (Ejercicio 8.3)
        ttk.Label(frame_form, text="Sueldo ($):").grid(row=4, column=0, sticky="w", pady=5, padx=5)
        vcmd = (self.root.register(self.validar_sueldo), '%P')
        self.txt_sueldo = ttk.Entry(frame_form, width=25, validate='key', validatecommand=vcmd)
        self.txt_sueldo.grid(row=4, column=1, sticky="w", pady=5, padx=5)

        # -------------------------------------------------------------------
        # 2. PANEL DE BOTONES
        # -------------------------------------------------------------------
        frame_botones = ttk.Frame(self.root, padding=(5, 5))
        frame_botones.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_botones, text="Guardar", command=self.guardar_empleado).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Modificar", command=self.modificar_empleado).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_empleado).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Limpiar Formulario", command=self.limpiar_formulario).pack(side="left", padx=5)

        # -------------------------------------------------------------------
        # 3. TABLA DE REGISTROS (Treeview)
        # -------------------------------------------------------------------
        frame_tabla = ttk.LabelFrame(self.root, text="Registros de Empleados", padding=(5, 5))
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        columnas = ("id", "nombre", "genero", "depto", "sueldo")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("genero", text="Género")
        self.tabla.heading("depto", text="Departamento")
        self.tabla.heading("sueldo", text="Sueldo ($)")

        self.tabla.column("id", width=100, anchor="center")
        self.tabla.column("nombre", width=250, anchor="w")
        self.tabla.column("genero", width=120, anchor="center")
        self.tabla.column("depto", width=150, anchor="center")
        self.tabla.column("sueldo", width=120, anchor="e")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Evento Doble Clic sobre la tabla (Ejercicio 8.3)
        self.tabla.bind("<Double-1>", self.cargar_registro)

        # -------------------------------------------------------------------
        # 4. PANEL DE ESTADÍSTICAS (Ejercicio 8.3)
        # -------------------------------------------------------------------
        frame_stats = ttk.Frame(self.root, padding=(10, 10))
        frame_stats.pack(fill="x", padx=10, pady=5)

        self.lbl_promedio = ttk.Label(frame_stats, text="Sueldo Promedio: $0.00", font=("Helvetica", 10, "bold"))
        self.lbl_promedio.pack(side="right", padx=15)

        self.lbl_total = ttk.Label(frame_stats, text="Total Empleados: 0", font=("Helvetica", 10, "bold"))
        self.lbl_total.pack(side="right", padx=15)

    # =======================================================================
    # MÉTODOS Y MANEJO DE EVENTOS
    # =======================================================================

    # Validación de entrada para el sueldo (Ejercicio 8.3)
    def validar_sueldo(self, texto):
        if texto == "":
            return True
        try:
            val = float(texto)
            return val >= 0
        except ValueError:
            return False

    # Validar campos vacíos
    def validar_campos(self):
        if not self.txt_id.get().strip() or not self.txt_nombre.get().strip() or not self.txt_sueldo.get().strip():
            messagebox.showwarning("Campos Incompletos", "Por favor complete todos los campos del formulario.")
            return False
        return True

    # Guardar nuevo empleado
    def guardar_empleado(self):
        if not self.validar_campos():
            return

        emp_id = self.txt_id.get().strip()
        nombre = self.txt_nombre.get().strip()
        genero = self.var_genero.get()
        depto = self.cb_depto.get()
        sueldo = f"{float(self.txt_sueldo.get()):.2f}"

        self.tabla.insert("", "end", values=(emp_id, nombre, genero, depto, sueldo))
        self.limpiar_formulario()
        self.actualizar_estadisticas()
        messagebox.showinfo("Éxito", "Empleado registrado exitosamente.")

    # Cargar datos al formulario con Doble Clic (Ejercicio 8.3)
    def cargar_registro(self, event):
        seleccion = self.tabla.selection()
        if seleccion:
            self.fila_seleccionada = seleccion[0]
            valores = self.tabla.item(self.fila_seleccionada, "values")

            self.txt_id.delete(0, tk.END)
            self.txt_id.insert(0, valores[0])

            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, valores[1])

            self.var_genero.set(valores[2])
            self.cb_depto.set(valores[3])

            self.txt_sueldo.delete(0, tk.END)
            self.txt_sueldo.insert(0, valores[4])

    # Modificar registro (Ejercicio 8.2)
    def modificar_empleado(self):
        if not self.fila_seleccionada or not self.tabla.exists(self.fila_seleccionada):
            messagebox.showwarning("Aviso", "Haga doble clic en una fila de la tabla para cargar y editar el registro.")
            return

        if not self.validar_campos():
            return

        emp_id = self.txt_id.get().strip()
        nombre = self.txt_nombre.get().strip()
        genero = self.var_genero.get()
        depto = self.cb_depto.get()
        sueldo = f"{float(self.txt_sueldo.get()):.2f}"

        self.tabla.item(self.fila_seleccionada, values=(emp_id, nombre, genero, depto, sueldo))
        self.limpiar_formulario()
        self.actualizar_estadisticas()
        messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

    # Eliminar registro (Ejercicio 8.2)
    def eliminar_empleado(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione una fila de la tabla para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar este registro?")
        if confirmar:
            self.tabla.delete(seleccion[0])
            self.limpiar_formulario()
            self.actualizar_estadisticas()
            messagebox.showinfo("Eliminado", "Empleado eliminado con éxito.")

    # Limpiar formulario (Ejercicio 8.2)
    def limpiar_formulario(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.var_genero.set("Masculino")
        self.cb_depto.current(0)
        self.txt_sueldo.delete(0, tk.END)
        self.fila_seleccionada = None
        if self.tabla.selection():
            self.tabla.selection_remove(self.tabla.selection())

    # Calcular y actualizar estadísticas (Ejercicio 8.3)
    def actualizar_estadisticas(self):
        filas = self.tabla.get_children()
        total = len(filas)
        suma_sueldos = 0.0

        for item_id in filas:
            valores = self.tabla.item(item_id, "values")
            suma_sueldos += float(valores[4])

        promedio = (suma_sueldos / total) if total > 0 else 0.0

        self.lbl_total.config(text=f"Total Empleados: {total}")
        self.lbl_promedio.config(text=f"Sueldo Promedio: ${promedio:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionEmpleadosGUI(root)
    root.mainloop()