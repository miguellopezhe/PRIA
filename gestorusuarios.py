import json
import os
from usuario import Usuario 

def datos(archivo):

    while True:
        dni = str(input("Introduce el DNI: "))
        nombre = str(input("Introduce el nombre: "))

        if comprobar_dni(dni): 
            añadir_usuario(archivo, dni, nombre)
            break
        else:
             print("\nERROR: Datos incorrectos. Introduce los datos de nuevo\n")

def añadir_usuario(archivo, dni, nombre):

    usuario = Usuario(dni, nombre).to_json()
        
    if not os.path.exists(archivo):
        datos = []
    else:
        datos = leer_json(archivo)

    datos.append(usuario)

    print("\nUsuario creado correctamente")

    with open(archivo, "w") as f: 
        json.dump(datos, f)
    
def mostrar_datos(archivo):
    datos = leer_json(archivo) 

    print("Lista de usuarios")
    for usuario in datos:
        print("DNI: " + usuario["dni"] + ", Nombre: " + usuario["nombre"])   
 
def leer_json(archivo):
    with open(archivo, "r") as f:
        datos = json.load(f)
    return datos  

def eliminar_usuario(archivo):
    True

def modificar_usuario(archivo):
    True   

def comprobar_dni(dni):

    if len(dni) != 9:
        return False

    for i in range(0, 7):
        if not dni[i].isdigit():
            return False
        
    if dni[8].isdigit():
        return False

    return True