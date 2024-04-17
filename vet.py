import tkinter as tk
from tkinter import messagebox

class VeterinariaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Clínica PetCare - Sistema de Veterinaria")
        
        self.color_verde = "#6A994E"
        self.color_rosa_claro = "#FFB6C1"
        self.color_secundario = "#FFFFFF"
        
        
        self.master.configure(bg=self.color_secundario)
        
       
        self.frame = tk.Frame(self.master, bg=self.color_secundario, padx=20, pady=20)
        self.frame.pack()

  
        self.nombre_veterinaria_label = tk.Label(self.frame, text="Clínica PetCare", font=("Arial", 20, "bold"), bg=self.color_secundario, fg=self.color_verde)
        self.nombre_veterinaria_label.grid(row=0, columnspan=2, pady=(0, 20))  # Añadido pady al grid

      
        self.nombre_label = tk.Label(self.frame, text="Nombre de la mascota:", font=("Arial", 12), bg=self.color_secundario)
        self.nombre_label.grid(row=1, column=0, sticky="e")
        self.nombre_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        self.especie_label = tk.Label(self.frame, text="Especie:", font=("Arial", 12), bg=self.color_secundario)
        self.especie_label.grid(row=2, column=0, sticky="e")
        self.especie_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.especie_entry.grid(row=2, column=1, padx=10, pady=5)

        self.raza_label = tk.Label(self.frame, text="Raza:", font=("Arial", 12), bg=self.color_secundario)
        self.raza_label.grid(row=3, column=0, sticky="e")
        self.raza_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.raza_entry.grid(row=3, column=1, padx=10, pady=5)

      
        self.registrar_button = tk.Button(self.frame, text="Registrar Mascota", font=("Arial", 12), bg=self.color_verde, fg=self.color_secundario, command=self.registrar_mascota)
        self.registrar_button.grid(row=4, columnspan=2, pady=10)

        self.buscar_label = tk.Label(self.frame, text="Buscar por nombre:", font=("Arial", 12), bg=self.color_secundario)
        self.buscar_label.grid(row=5, column=0, sticky="e")
        self.buscar_entry = tk.Entry(self.frame, font=("Arial", 12))
        self.buscar_entry.grid(row=5, column=1, padx=10, pady=5)

        self.buscar_button = tk.Button(self.frame, text="Buscar", font=("Arial", 12), bg=self.color_verde, fg=self.color_secundario, command=self.buscar_mascota)
        self.buscar_button.grid(row=6, columnspan=2, pady=5)

        self.registros_label = tk.Label(self.frame, text="Mascotas registradas:", font=("Arial", 12), bg=self.color_secundario)
        self.registros_label.grid(row=7, column=0, columnspan=2, pady=(20, 5))

        self.registros_listbox = tk.Listbox(self.frame, font=("Arial", 12), width=40, height=10)
        self.registros_listbox.grid(row=8, column=0, columnspan=2)

      
        self.editar_button = tk.Button(self.frame, text="Editar", font=("Arial", 12), bg=self.color_verde, fg=self.color_secundario, command=self.editar_mascota)
        self.editar_button.grid(row=9, column=0, padx=5, pady=5)

        self.eliminar_button = tk.Button(self.frame, text="Eliminar", font=("Arial", 12), bg=self.color_verde, fg=self.color_secundario, command=self.eliminar_mascota)
        self.eliminar_button.grid(row=9, column=1, padx=5, pady=5)

        self.mascotas = [
            {"nombre": "Luna", "especie": "Perro", "raza": "Labrador Retriever"},
            {"nombre": "Milo", "especie": "Gato", "raza": "Siamés"}
        ]
        self.actualizar_lista_mascotas()

    def registrar_mascota(self):
        nombre = self.nombre_entry.get()
        especie = self.especie_entry.get()
        raza = self.raza_entry.get()

        if nombre and especie and raza:
            nueva_mascota = {"nombre": nombre, "especie": especie, "raza": raza}
            self.mascotas.append(nueva_mascota)
            self.actualizar_lista_mascotas()
            messagebox.showinfo("Éxito", "Mascota registrada correctamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")

    def buscar_mascota(self):
        nombre_buscar = self.buscar_entry.get()
        if nombre_buscar:
            mascotas_encontradas = [mascota for mascota in self.mascotas if mascota["nombre"].lower() == nombre_buscar.lower()]
            if mascotas_encontradas:
                messagebox.showinfo("Mascotas encontradas", "\n".join([f"Nombre: {m['nombre']}, Especie: {m['especie']}, Raza: {m['raza']}" for m in mascotas_encontradas]))
            else:
                messagebox.showinfo("Mascotas encontradas", "No se encontraron mascotas con ese nombre.")
        else:
            messagebox.showerror("Error", "Por favor ingrese un nombre para buscar.")

    def editar_mascota(self):
        seleccionado = self.registros_listbox.curselection()
        if seleccionado:
            indice = seleccionado[0]
            mascota_seleccionada = self.mascotas[indice]
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, mascota_seleccionada["nombre"])
            self.especie_entry.delete(0, tk.END)
            self.especie_entry.insert(0, mascota_seleccionada["especie"])
            self.raza_entry.delete(0, tk.END)
            self.raza_entry.insert(0, mascota_seleccionada["raza"])
            messagebox.showinfo("Edición", "Los datos de la mascota están listos para ser editados.")
        else:
            messagebox.showerror("Error", "Por favor seleccione una mascota de la lista para editar.")

    def eliminar_mascota(self):
        seleccionado = self.registros_listbox.curselection()
        if seleccionado:
            indice = seleccionado[0]
            del self.mascotas[indice]
            self.actualizar_lista_mascotas()
            messagebox.showinfo("Eliminación", "La mascota seleccionada ha sido eliminada.")
        else:
            messagebox.showerror("Error", "Por favor seleccione una mascota de la lista para eliminar.")

    def actualizar_lista_mascotas(self):
        self.registros_listbox.delete(0, tk.END)
        for mascota in self.mascotas:
            self.registros_listbox.insert(tk.END, f"{mascota['nombre']} - {mascota['especie']} - {mascota['raza']}")

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.especie_entry.delete(0, tk.END)
        self.raza_entry.delete(0, tk.END)
        

def main():
    root = tk.Tk()
    app = VeterinariaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
