import json
import os

from usuario import Usuario

def datos(archivo):
    dni = str(input("Introduce el DNI: "))
    while True:  
        if comprobar_dni(dni): 
            print("\nERROR: DNI incorrecto. Introduce los datos de nuevo\n")
            dni = str(input("Introduce el DNI: "))

        if dni_repite(archivo,dni):
                print("\nERROR: DNI repetido. Introduce los datos de nuevo\n")
                dni = str(input("Introduce el DNI: "))
        else:      
            break

    nombre = str(input("Introduce el nombre: "))
    while True:
        if comprobar_nombre(nombre): 
            print("\nERROR: Nombre incorrecto. Introduce los datos de nuevo\n")
            nombre = str(input("Introduce el nombre: "))
        else:       
            break  

    dni = dni.upper() 
    nombre = nombre.capitalize()
    añadir_usuario(archivo, dni, nombre) 

def añadir_usuario(archivo, dni, nombre):
    usuario = Usuario(dni, nombre).to_json()
        
    if not os.path.exists(archivo):
        datos = []
    else:
        datos = leer_json(archivo)

    datos.append(usuario)

    print("\nUsuario creado correctamente")

    guardar_datos(archivo, datos)
    
def mostrar_datos(archivo):

    try:
        datos = leer_json(archivo) 

        print("Lista de usuarios")
        for usuario in datos:
            print("DNI: " + usuario["dni"] + ", Nombre: " + usuario["nombre"])   
    except:
        print("No existe el archivo")

def leer_json(archivo):
    with open(archivo, "r") as f:
        datos = json.load(f)
    return datos  

def eliminar_usuario(archivo):
    dni = str(input("Introduce el dni para eliminar el usuario: "))

    datos = leer_json(archivo)

    contador = 0
    for usuario in datos:
        if usuario["dni"] == dni:
            del datos[contador]
            guardar_datos(archivo, datos)
            print("\nUsuario eliminado correctamente.")    
            break
        contador += 1
    print("\nUsuario no encontrado.")
    
def modificar_usuario(archivo):
    dni = str(input("Introduce el dni para modificar: "))

    datos = leer_json(archivo)
    contador = 0
    for usuario in datos:
        if usuario["dni"] == dni:
            dni = input("Introduce el DNI: ")
            nombre = input("Introduce el nombre: ")
            datos[contador]["dni"] = dni
            datos[contador]["nombre"] = nombre
            guardar_datos(archivo, datos)      
        contador += 1
    print("\nUsuario no encontrado.")

def comprobar_dni(dni):
    if len(dni) != 9:
        return True

    for i in range(0, 7):
        if not dni[i].isdigit():
            return True
        
    if dni[8].isdigit():
        return True
    
    return False

def guardar_datos(archivo, datos):
    with open(archivo, "w") as f: 
        json.dump(datos, f, indent=2)

def comprobar_nombre(nombre):
    if nombre.isdigit() | len(nombre) == 0:
        return True
    else:
        return False

def que_modificar():
    True

def dni_repite(archivo, dni):
    datos = leer_json(archivo)
    
    dni = dni.upper()
    for usuario in datos:
        if usuario["dni"] == dni:
            return True
            
    return False

