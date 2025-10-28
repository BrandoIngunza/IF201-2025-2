import tkinter as tk
from Gestor_Archivos import Archivo
from tkinter import ttk, messagebox

class Ventana:
    def __init__(self, root):
        self.root = root
        self.root.title("Productos")
        self.root.geometry("600x400")
        self.archivo = Archivo('Producto.txt')
        self.archivo.abrir()
        self.arreglo_datos = self.archivo.mostrar()
        
        self.txt_nombre = tk.StringVar()
        self.txt_nombre.set('---------')
        self.txt_precio = tk.StringVar()
        self.txt_precio.set('---------')
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=5)
        
        self.frame_btn = tk.Frame(self.root)
        self.frame_btn.pack()
        
        tk.Label(self.frame, text= 'Codigo:', fg='black').grid(row=0,column=0, sticky = 'w')
        tk.Label(self.frame, text= 'Nombre:', fg='black').grid(row=1,column=0, sticky= 'w')
        tk.Label(self.frame, text= 'Precio:', fg='black').grid(row=2,column=0, sticky= 'w')
        self.lbl_nombre = tk.Label(self.frame, textvariable= self.txt_nombre, fg='black')
        self.lbl_nombre.grid(row=1,column=1, sticky='w')
        self.lbl_precio = tk.Label(self.frame, textvariable= self.txt_precio, fg='black')
        self.lbl_precio.grid(row=2,column=1, sticky='w')
        
        self.entry = tk.Entry(self.frame)
        self.entry.grid(row=0,column=1, sticky='w')
    
        self.btn_buscar= tk.Button(self.frame_btn, text="BUSCAR", command=self.buscar)
        self.btn_buscar.grid(row=3,column=0, padx=5)
        
        self.btn_minorPrice = tk.Button(self.frame_btn, text="PRECIO MENOR", command=self.minorPrice)
        self.btn_minorPrice.grid(row=3,column=1, padx=5)
        
        self.btn_sum = tk.Button(self.frame_btn, text="SUMAR", command=self.sum)
        self.btn_sum.grid(row=3,column=2, padx=5)
    
        # self.tree = ttk.Treeview(self.root)
        # # self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree = ttk.Treeview(self.root, columns=("Codigo", "Nombre",
            "Precio"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.capitalize())
            self.tree.pack(expand=True, fill="both", pady=10)
        
        self.cargar_datos()
    
    def buscar(self):
        try:
            codigo = int(self.entry.get())
            # messagebox.showinfo('GAAA', codigo)
            for linea in self.arreglo_datos:
                if codigo == int(linea[0]):
                   self.txt_nombre.set(linea [1])
                   self.txt_precio.set(linea [2])
                   return
            messagebox.showwarning('Codigo', f'No se encontro el codigo {codigo}')
            self.txt_nombre.set('--------')
            self.txt_precio.set('--------')
        except ValueError:
            messagebox.showerror(f"Error", "El dato tiene que ser entero")
    def minorPrice(self):
        precio = 999
        for linea in self.arreglo_datos:
            if float(linea[2]) < precio:
                precio = float(linea[2])
        
        messagebox.showinfo('Precio', f'el menor precio es : {precio}')
    
    def sum(self):
        suma = 0
        for linea in self.arreglo_datos:
            suma += float(linea[2])
        messagebox.showinfo('Suma', f'La suma es: {suma}')    
    def cargar_datos(self):
        for fila in self.arreglo_datos:
            self.tree.insert("", tk.END, value=fila)
            

if __name__ == "__main__":        
    root = tk.Tk()
    Ventana(root)
    root.mainloop()