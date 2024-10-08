import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import sqlite3

class FormularioPersonal:
    def __init__(self):
        self.conexion = sqlite3.connect("taller_1.db")  
        
        self.crear_tabla()

        self.ventana = tk.Tk()
        self.ventana.title("Formulario de Personal")
        
        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.presentacion_var = tk.StringVar()
        self.fecha_var = tk.StringVar()
        self.laboratorio_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()

        self.crear_widgets()
        self.ventana.mainloop()

    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS persona (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            nombre TEXT NOT NULL,
            presentacion TEXT NOT NULL,
            fecha_vencimiento TEXT NOT NULL,
            laboratorio TEXT NOT NULL,
            cantidad INTEGER NOT NULL
        )
        ''')
        self.conexion.commit()

    def crear_widgets(self):
        ttk.Label(self.ventana, text="Código de Producto:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.ventana, textvariable=self.codigo_var).grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.ventana, text="Nombre de Producto:").grid(column=0, row=1, padx=10, pady=10)
        ttk.Entry(self.ventana, textvariable=self.nombre_var).grid(column=1, row=1, padx=10, pady=10)

        ttk.Label(self.ventana, text="Presentación:").grid(column=0, row=2, padx=10, pady=10)
        ttk.Entry(self.ventana, textvariable=self.presentacion_var).grid(column=1, row=2, padx=10, pady=10)
        
        ttk.Label(self.ventana, text="Fecha de Vencimiento:").grid(column=0, row=3, padx=10, pady=10)
        ttk.Entry(self.ventana, textvariable=self.fecha_var).grid(column=1, row=3, padx=10, pady=10)
        
        ttk.Label(self.ventana, text="Laboratorio:").grid(column=0, row=4, padx=10, pady=10)
        ttk.Entry(self.ventana, textvariable=self.laboratorio_var).grid(column=1, row=4, padx=10, pady=10)
        
        ttk.Label(self.ventana, text="Cantidad en Bodega:").grid(column=0, row=5, padx=10, pady=10)
        ttk.Entry(self.ventana, textvariable=self.cantidad_var).grid(column=1, row=5, padx=10, pady=10)

        ttk.Button(self.ventana, text="Guardar", command=self.guardar).grid(column=1, row=6, padx=10, pady=10)

    def guardar(self):
        codigo = self.codigo_var.get()
        nombre = self.nombre_var.get()
        presentacion = self.presentacion_var.get()
        fecha_vencimiento = self.fecha_var.get()
        laboratorio = self.laboratorio_var.get()
        cantidad = self.cantidad_var.get()
        
        if not codigo or not nombre or not presentacion or not fecha_vencimiento or not laboratorio or not cantidad:
            mb.showwarning("Advertencia", "Completa todos los campos para continuar")
            return

        cursor = self.conexion.cursor()
        cursor.execute("INSERT INTO persona(codigo, nombre, presentacion, fecha_vencimiento, laboratorio, cantidad) VALUES (?, ?, ?, ?, ?, ?)", 
                       (codigo, nombre, presentacion, fecha_vencimiento, laboratorio, cantidad))
        self.conexion.commit()
        
        mb.showinfo("Información", "Datos guardados exitosamente.")
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.presentacion_var.set("")
        self.fecha_var.set("")
        self.laboratorio_var.set("")
        self.cantidad_var.set("")

    def __del__(self):
        self.conexion.close()

# Inicializar la aplicación
if __name__ == "__main__":
    FormularioPersonal()
