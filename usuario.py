from libro import Libro
from usuario import Usuario

lista_libros = []
lista_usuarios = []
cola_prestamos = []
pila_devoluciones = []

def agregar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    libro = Libro(titulo, autor, isbn)
    lista_libros.append(libro)
    print("✅ Libro agregado.")

def registrar_usuario():
    nombre = input("Nombre del usuario: ")
    id_usuario = input("ID del usuario: ")
    usuario = Usuario(nombre, id_usuario)
    lista_usuarios.append(usuario)
    print("✅ Usuario registrado.")

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
            print("📚 Libro prestado.")
        else:
            print("❌ Libro no disponible.")
    else:
        print("❌ Usuario o libro no encontrado.")

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
            print("🔁 Libro devuelto.")
        else:
            print("❌ El usuario no tiene ese libro.")
    else:
        print("❌ Usuario no encontrado.")

def menu():
    while True:
        print("\n📚 MENU BIBLIOTECA 📚")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❗ Opción inválida.")

# Iniciar el menú
menu()
