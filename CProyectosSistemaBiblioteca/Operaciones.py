from libro import Libro
from usuario import Usuario

lista_libros = []
lista_usuarios = []
cola_prestamos = []
pila_devoluciones = []

def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    if any(l.isbn == isbn for l in lista_libros):
        print("ISBN ya registrado.")
        return
    lista_libros.append(Libro(titulo, autor, isbn))
    print("Libro agregado.")

def registrar_usuario():
    nombre = input("Nombre del usuario: ")
    id_usuario = input("ID del usuario: ")
    if any(u.id_usuario == id_usuario for u in lista_usuarios):
        print("ID ya registrado.")
        return
    lista_usuarios.append(Usuario(nombre, id_usuario))
    print("Usuario registrado.")

def listar_libros():
    if not lista_libros:
        print("No hay libros.")
    for libro in lista_libros:
        print(libro)

def listar_usuarios():
    if not lista_usuarios:
        print("No hay usuarios.")
    for usuario in lista_usuarios:
        print(usuario)

def prestar_libro():
    id_usuario = input("ID del usuario: ")
    isbn = input("ISBN del libro: ")
    libro = next((l for l in lista_libros if l.isbn == isbn), None)
    usuario = next((u for u in lista_usuarios if u.id_usuario == id_usuario), None)
    if libro and usuario:
        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            cola_prestamos.append((id_usuario, isbn))
            print(f"Prestado: {libro.titulo} a {usuario.nombre}")
        else:
            print("Libro no disponible.")
    else:
        print("Usuario o libro no encontrado.")

def devolver_libro():
    id_usuario = input("ID del usuario: ")
    isbn = input("ISBN del libro: ")
    usuario = next((u for u in lista_usuarios if u.id_usuario == id_usuario), None)
    if usuario:
        libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
        if libro:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            pila_devoluciones.append((id_usuario, isbn))
            print(f"Devuelto: {libro.titulo} por {usuario.nombre}")
        else:
            print("El usuario no tiene ese libro.")
    else:
        print("Usuario no encontrado.")

def mostrar_estructuras():
    print("\n--- Estructuras actuales ---")
    print("Lista de libros:", [str(l) for l in lista_libros])
    print("Lista de usuarios:", [str(u) for u in lista_usuarios])
    print("Cola de préstamos:", cola_prestamos)
    print("Pila de devoluciones:", pila_devoluciones)
