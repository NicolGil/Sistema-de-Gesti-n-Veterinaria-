import tkinter as tk
from tkinter import simpledialog, messagebox

class VeterinariaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Veterinaria App")
        self.master.geometry("600x400")

        # Definición de colores
        self.color_verde = "#6A994E"
        self.color_blanco = "#FFFFFF"
        
        # Configuración del tema
        self.master.configure(bg=self.color_blanco)
        
        # Frame principal
        self.frame = tk.Frame(self.master, bg=self.color_blanco)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Menu superior
        self.menu_frame = tk.Frame(self.frame, bg=self.color_verde)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)

        # Opciones del menú
        opciones_menu = ["Clientes", "Mascotas", "Citas"]
        self.botones_menu = []
        for opcion in opciones_menu:
            boton = tk.Button(self.menu_frame, text=opcion, font=("Arial", 12), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.mostrar_opcion(o))
            boton.pack(side=tk.LEFT, padx=10, pady=5)
            self.botones_menu.append(boton)

        # Campos para la lista de elementos
        self.lista_frame = tk.Frame(self.frame, bg=self.color_blanco)
        self.lista_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        # Lista de elementos
        self.lista_label = tk.Label(self.lista_frame, text="", font=("Arial", 12), bg=self.color_blanco)
        self.lista_label.pack(expand=True, fill=tk.BOTH)

        # Datos de ejemplo
        self.clientes = [{"nombre": "Juan", "telefono": "123456789"}, {"nombre": "Ana", "telefono": "987654321"}]
        self.mascotas = [{"nombre": "Luna", "especie": "Perro", "raza": "Labrador", "dueño": "Juan"}, {"nombre": "Milo", "especie": "Gato", "raza": "Siamés", "dueño": "Ana"}]
        self.citas = [{"fecha": "01/04/2024", "hora": "10:00", "mascota": "Luna"}, {"fecha": "02/04/2024", "hora": "11:00", "mascota": "Milo"}]

    def mostrar_opcion(self, opcion):
        self.limpiar_lista()
        if opcion == "Clientes":
            self.mostrar_lista_clientes()
        elif opcion == "Mascotas":
            self.mostrar_lista_mascotas()
        elif opcion == "Citas":
            self.mostrar_lista_citas()

    def limpiar_lista(self):
        self.lista_label.config(text="")

    def mostrar_lista_clientes(self):
        self.limpiar_lista()
        self.lista_label.config(text="Lista de Clientes:\n\n")
        for cliente in self.clientes:
            self.lista_label.config(text=self.lista_label.cget("text") + f"Nombre: {cliente['nombre']}, Teléfono: {cliente['telefono']}\n")
        
        # Agregar botones para acciones de cliente
        self.agregar_botones_accion("Clientes")

    def mostrar_lista_mascotas(self):
        self.limpiar_lista()
        self.lista_label.config(text="Lista de Mascotas:\n\n")
        for mascota in self.mascotas:
            self.lista_label.config(text=self.lista_label.cget("text") + f"Nombre: {mascota['nombre']}, Especie: {mascota['especie']}, Raza: {mascota['raza']}, Dueño: {mascota['dueño']}\n")
        
        # Agregar botones para acciones de mascota
        self.agregar_botones_accion("Mascotas")

    def mostrar_lista_citas(self):
        self.limpiar_lista()
        self.lista_label.config(text="Lista de Citas:\n\n")
        for cita in self.citas:
            self.lista_label.config(text=self.lista_label.cget("text") + f"Fecha: {cita['fecha']}, Hora: {cita['hora']}, Mascota: {cita['mascota']}\n")
        
        # Agregar botones para acciones de cita
        self.agregar_botones_accion("Citas")

    def agregar_botones_accion(self, opcion):
        boton_agregar = tk.Button(self.lista_frame, text="Agregar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.agregar_elemento(o))
        boton_agregar.pack(side=tk.LEFT, padx=10, pady=5)
        
        if opcion == "Clientes":
            boton_editar = tk.Button(self.lista_frame, text="Editar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.editar_elemento(o))
            boton_editar.pack(side=tk.LEFT, padx=10, pady=5)
            boton_eliminar = tk.Button(self.lista_frame, text="Eliminar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.eliminar_elemento(o))
            boton_eliminar.pack(side=tk.LEFT, padx=10, pady=5)
        elif opcion == "Mascotas":
            boton_editar = tk.Button(self.lista_frame, text="Editar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.editar_elemento(o))
            boton_editar.pack(side=tk.LEFT, padx=10, pady=5)
            boton_eliminar = tk.Button(self.lista_frame, text="Eliminar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.eliminar_elemento(o))
            boton_eliminar.pack(side=tk.LEFT, padx=10, pady=5)
        elif opcion == "Citas":
            boton_editar = tk.Button(self.lista_frame, text="Editar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.editar_elemento(o))
            boton_editar.pack(side=tk.LEFT, padx=10, pady=5)
            boton_eliminar = tk.Button(self.lista_frame, text="Eliminar", font=("Arial", 10), bg=self.color_blanco, fg=self.color_verde, command=lambda o=opcion: self.eliminar_elemento(o))
            boton_eliminar.pack(side=tk.LEFT, padx=10, pady=5)

    def agregar_elemento(self, opcion):
        if opcion == "Clientes":
            nombre = simpledialog.askstring("Agregar Cliente", "Ingrese el nombre del cliente:")
            telefono = simpledialog.askstring("Agregar Cliente", "Ingrese el teléfono del cliente:")
            if nombre and telefono:
                self.clientes.append({"nombre": nombre, "telefono": telefono})
                self.mostrar_lista_clientes()
            else:
                messagebox.showerror("Error", "Por favor complete todos los campos.")
        elif opcion == "Mascotas":
            nombre = simpledialog.askstring("Agregar Mascota", "Ingrese el nombre de la mascota:")
            especie = simpledialog.askstring("Agregar Mascota", "Ingrese la especie de la mascota:")
            raza = simpledialog.askstring("Agregar Mascota", "Ingrese la raza de la mascota:")
            dueno = simpledialog.askstring("Agregar Mascota", "Ingrese el dueño de la mascota:")
            if nombre and especie and raza and dueno:
                self.mascotas.append({"nombre": nombre, "especie": especie, "raza": raza, "dueño": dueno})
                self.mostrar_lista_mascotas()
            else:
                messagebox.showerror("Error", "Por favor complete todos los campos.")
        elif opcion == "Citas":
            fecha = simpledialog.askstring("Agendar Cita", "Ingrese la fecha de la cita:")
            hora = simpledialog.askstring("Agendar Cita", "Ingrese la hora de la cita:")
            mascota = simpledialog.askstring("Agendar Cita", "Ingrese el nombre de la mascota para la cita:")
            if fecha and hora and mascota:
                self.citas.append({"fecha": fecha, "hora": hora, "mascota": mascota})
                self.mostrar_lista_citas()
            else:
                messagebox.showerror("Error", "Por favor complete todos los campos.")

    def editar_elemento(self, opcion):
        pass

    def eliminar_elemento(self, opcion):
        pass

def main():
    root = tk.Tk()
    app = VeterinariaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
