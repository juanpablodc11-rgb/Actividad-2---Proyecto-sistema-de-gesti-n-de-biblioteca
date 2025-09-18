from operaciones import (
    agregar_libro, registrar_usuario, listar_libros, listar_usuarios,
    prestar_libro, devolver_libro, mostrar_estructuras,
    lista_libros, lista_usuarios, Libro, Usuario
)

# Precargar datos reales
lista_libros.extend([
    Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728"),
    Libro("El principito", "Antoine de Saint-Exupéry", "978-0156012195"),
    Libro("1984", "George Orwell", "978-0451524935"),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8491050297")
])

lista_usuarios.extend([
    Usuario("Ana Pérez", "U001"),
    Usuario("Carlos Gómez", "U002"),
    Usuario("Lucía Martínez", "U003")
])

def menu():
    while True:
        print("\n MENU BIBLIOTECA ")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Listar libros")
        print("4. Listar usuarios")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Mostrar estructuras")
        print("8. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1": agregar_libro()
        elif opcion == "2": registrar_usuario()
        elif opcion == "3": listar_libros()
        elif opcion == "4": listar_usuarios()
        elif opcion == "5": prestar_libro()
        elif opcion == "6": devolver_libro()
        elif opcion == "7": mostrar_estructuras()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
