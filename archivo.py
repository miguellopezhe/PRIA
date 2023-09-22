import json

nombre_archivo = "usuarios.json"

class Usuario:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
    
    def to_json(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
        }

def leer_json(archivo):
    with open(archivo, "r") as f:
        datos = json.load(f)
        return datos
    
def mostrar_datos(archivo):
    datos = leer_json(archivo)
    print(leer_json("Nombre: " + str(datos["nombre"])))


def crear_usuario(archivo):
    datos = leer_json(archivo)

    dni = str(input("Introduce el DNI: "))
    nombre = str(input("Introduce el nombre: "))

    usuario = Usuario(dni, nombre)

    datos.append(usuario.to_json())

    with open(archivo, "w") as f:
        json.dump(datos, f)   
    
crear_usuario(nombre_archivo)
mostrar_datos(nombre_archivo)