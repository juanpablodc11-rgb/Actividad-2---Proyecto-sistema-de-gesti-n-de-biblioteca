import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# ==== CLASES ====
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

class Usuario:
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo
        self.libros_prestados = []

# ==== DATOS PREDETERMINADOS ====
lista_libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728"),
    Libro("El principito", "Antoine de Saint-Exupéry", "978-0156012195"),
    Libro("1984", "George Orwell", "978-0451524935"),
    Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "978-8478884452"),
]
lista_usuarios = [
    Usuario("Ana Pérez", "U001", "ana@example.com"),
    Usuario("Carlos Gómez", "U002", "carlos@example.com"),
]

cola_prestamos = []
pila_devoluciones = []

# ==== FUNCIONES ====
def actualizar_listas():
    # Actualizar tabla de libros
    for item in libros_tree.get_children():
        libros_tree.delete(item)
    for l in lista_libros:
        estado = "Disponible" if l.disponible else "Prestado"
        libros_tree.insert("", tk.END, values=(l.titulo, l.autor, l.isbn, estado))

    # Actualizar tabla de usuarios
    for item in usuarios_tree.get_children():
        usuarios_tree.delete(item)
    for u in lista_usuarios:
        usuarios_tree.insert("", tk.END, values=(u.nombre, u.id_usuario, u.correo, len(u.libros_prestados)))

def agregar_libro():
    titulo = simpledialog.askstring("Agregar libro", "Título:")
    autor = simpledialog.askstring("Agregar libro", "Autor:")
    isbn = simpledialog.askstring("Agregar libro", "ISBN:")
    if not (titulo and autor and isbn):
        return
    if any(l.isbn == isbn for l in lista_libros):
        messagebox.showerror("Error", "El ISBN ya existe.")
        return
    lista_libros.append(Libro(titulo, autor, isbn))
    actualizar_listas()
    messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado.")

def registrar_usuario():
    nombre = simpledialog.askstring("Registrar usuario", "Nombre:")
    uid = simpledialog.askstring("Registrar usuario", "ID:")
    correo = simpledialog.askstring("Registrar usuario", "Correo electrónico:")
    if not (nombre and uid and correo):
        return
    if any(u.id_usuario == uid for u in lista_usuarios):
        messagebox.showerror("Error", "El ID ya existe.")
        return
    lista_usuarios.append(Usuario(nombre, uid, correo))
    actualizar_listas()
    messagebox.showinfo("Éxito", f"Usuario '{nombre}' registrado.")

def prestar_libro():
    uid = simpledialog.askstring("Prestar libro", "ID del usuario:")
    isbn = simpledialog.askstring("Prestar libro", "ISBN del libro:")
    usuario = next((u for u in lista_usuarios if u.id_usuario == uid), None)
    libro = next((l for l in lista_libros if l.isbn == isbn), None)
    if not usuario or not libro:
        messagebox.showerror("Error", "Usuario o libro no encontrado.")
        return
    if not libro.disponible:
        messagebox.showerror("Error", "El libro no está disponible.")
        return
    libro.disponible = False
    usuario.libros_prestados.append(libro)
    cola_prestamos.append((uid, isbn))
    actualizar_listas()
    messagebox.showinfo("Éxito", f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

def devolver_libro():
    uid = simpledialog.askstring("Devolver libro", "ID del usuario:")
    isbn = simpledialog.askstring("Devolver libro", "ISBN del libro:")
    usuario = next((u for u in lista_usuarios if u.id_usuario == uid), None)
    if not usuario:
        messagebox.showerror("Error", "Usuario no encontrado.")
        return
    libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
    if not libro:
        messagebox.showerror("Error", "Ese usuario no tiene ese libro.")
        return
    libro.disponible = True
    usuario.libros_prestados.remove(libro)
    pila_devoluciones.append((uid, isbn))
    actualizar_listas()
    messagebox.showinfo("Éxito", f"Libro '{libro.titulo}' devuelto.")

# ==== INTERFAZ ====
root = tk.Tk()
root.title("📚 Biblioteca Funcional")

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=5)
tk.Button(frame_botones, text="Agregar Libro", command=agregar_libro).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Registrar Usuario", command=registrar_usuario).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Prestar Libro", command=prestar_libro).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Devolver Libro", command=devolver_libro).grid(row=0, column=3, padx=5)

# Tabla de libros
tk.Label(root, text="Libros").pack()
libros_tree = ttk.Treeview(root, columns=("Título","Autor","ISBN","Estado"), show="headings", height=6)
for col in ("Título","Autor","ISBN","Estado"):
    libros_tree.heading(col, text=col)
libros_tree.pack(fill=tk.BOTH, expand=True)

# Tabla de usuarios
tk.Label(root, text="Usuarios").pack()
usuarios_tree = ttk.Treeview(root, columns=("Nombre","ID","Correo","Prestados"), show="headings", height=6)
for col in ("Nombre","ID","Correo","Prestados"):
    usuarios_tree.heading(col, text=col)
usuarios_tree.pack(fill=tk.BOTH, expand=True)

actualizar_listas()
root.mainloop()
