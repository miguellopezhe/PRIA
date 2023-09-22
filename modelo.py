import json

class Usuario:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = str(nombre).capitalize()
        self.apellido = apellido.capitalize()

class GestorUsuarios:
    def __init__(self, archivo):
        self.archivo = archivo
        self.usuarios = []

    def comprobar_dni(self, dni):
        if len(dni) != 8:
            while True:
                print("El DNI debe ser de 8 carácteres.")
                dni = input("Ingrese un DNI de usuario válido: ")
                if len(dni) == 8:
                    break

    def cargar_usuarios(self):
        try:
            with open(self.archivo, 'r') as f:
                usuarios_data = json.load(f)
                self.usuarios = [Usuario(**data) for data in usuarios_data]
        except FileNotFoundError:
            self.usuarios = []

    def guardar_usuarios(self):
        usuarios_serializables = [usuario.__dict__ for usuario in self.usuarios]
        with open(self.archivo, 'w') as f:
            json.dump(usuarios_serializables, f)

    def agregar_usuario(self, dni, nombre, apellido):
        while True:
            self.comprobar_dni(dni)
            if not any(usuario.dni == dni for usuario in self.usuarios):
                nuevo_usuario = Usuario(dni, nombre, apellido)
                self.usuarios.append(nuevo_usuario)
                self.guardar_usuarios()
                break
            else:
                print("El DNI ya existe.")
                dni = input("Ingrese un DNI válido: ")
                


    def eliminar_usuario(self, dni):
        self.usuarios = [u for u in self.usuarios if u.dni != dni]
        self.guardar_usuarios()

    def modificar_usuario(self, dni, nombre, apellido):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                usuario.nombre = nombre
                usuario.apellido = apellido
                break
        self.guardar_usuarios()

    def obtener_todos_los_usuarios(self):
        return self.usuarios

if __name__ == "__main__":
    print("Estas ejecutando \"modelo.py\"\nEl programa se ejecuta desde controlador.")