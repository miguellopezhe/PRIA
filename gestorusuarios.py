import json
import os

from usuario import Usuario
rojo = "\033[31m"
negro = "\033[0m"
verde = "\033[32m"

def datos(archivo):
    dni = str(input("Introduce el DNI: "))
    while True:  
        if comprobar_dni(dni): 
            print(rojo,"\nERROR: DNI incorrecto. Introduce los datos de nuevo\n",negro)
            dni = str(input("Introduce el DNI: "))
            comprobardni = False
        else:
            comprobardni = True

        if dni_repite(archivo,dni):
            print(rojo,"\nERROR: DNI repetido. Introduce los datos de nuevo\n",negro)
            dni = str(input("Introduce el DNI: "))
            comprobarnombre = False
        else:
            comprobarnombre = True

        if comprobardni & comprobarnombre:      
            break

    nombre = str(input("Introduce el nombre: "))
    while True:
        if comprobar_nombre(nombre): 
            print(rojo,"\nERROR: Nombre incorrecto. Introduce los datos de nuevo\n",negro)
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

    print(verde,"\nUsuario creado correctamente",negro)

    guardar_datos(archivo, datos)
    
def mostrar_datos(archivo):

    try:
        datos = leer_json(archivo) 
        datosordenados = ordenar_json(datos)
        print("Lista de usuarios")
        for usuario in datosordenados:
            print("DNI: " + usuario["dni"] + ", Nombre: " + usuario["nombre"])   
    except:
        print(rojo,"No existe el archivo",negro)

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
            print(verde,"\nUsuario eliminado correctamente.",negro)    
            break
        contador += 1
    print(rojo,"\nUsuario no encontrado.",negro)
    
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
    print(rojo,"\nUsuario no encontrado.",negro)

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
    if nombre.isdigit():
        return True
    
    if len(nombre) == 0:
        return True
    
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

def ordenar_json(datos):
    return sorted(datos, key=lambda x: x["nombre"])