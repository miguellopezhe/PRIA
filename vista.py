class Vista:
    @staticmethod
    def mostrar_menu():
        print("\n1. Mostrar todos los usuarios")
        print("2. Agregar usuario")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

    @staticmethod
    def obtener_datos_usuario():
        dni = input("Ingrese el DNI del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        return dni, nombre, apellido

    @staticmethod
    def mostrar_usuarios(usuarios):
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario.nombre)
            i = 0
            for usuario in usuarios_ordenados:
                i += 1        
                print(str(i) + "- " + str(usuario.dni) + " " + usuario.nombre + " " + usuario.apellido)
            

if __name__ == "__main__":
    print("Estas ejecutando \"vista.py\"\nEl programa se ejecuta desde controlador.")