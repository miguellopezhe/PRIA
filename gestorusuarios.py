import json
from usuario import Usuario
rojo = "\033[31m"
negro = "\033[0m"
verde = "\033[32m"

def recoger_datos(archivo):
    dni = str(input("Introduce el DNI: "))
    while True:  
        if comprobar_dni(dni): 
            print(rojo,"\nERROR: DNI incorrecto. Introduce los datos de nuevo.\n",negro)
            dni = str(input("Introduce el DNI: "))
            comprobardni = False
        else:
            comprobardni = True

        if dni_repite(archivo,dni):
            print(rojo,"\nERROR: DNI repetido. Introduce los datos de nuevo.\n",negro)
            dni = str(input("Introduce el DNI: "))
            comprobarnombre = False
        else:
            comprobarnombre = True

        if comprobardni & comprobarnombre:      
            break

    nombre = str(input("Introduce el nombre: "))
    while True:
        if comprobar_nombre(nombre): 
            print(rojo,"\nERROR: Nombre incorrecto. Introduce los datos de nuevo.\n",negro)
            nombre = str(input("Introduce el nombre: "))
        else:       
            break  

    dni = dni.upper() 
    nombre = nombre.capitalize()
    return dni, nombre

def agregar_usuario(archivo):

    dni, nombre = recoger_datos(archivo)

    usuario = Usuario(dni, nombre).to_json()    
  
    datos = leer_json(archivo)

    datos.append(usuario)

    print(verde,"\nUsuario creado correctamente.",negro)

    guardar_datos(archivo, datos)
    
def mostrar_datos(archivo):
    try:
        datos = leer_json(archivo) 
        if len(datos) == 0:
            print(rojo,"No hay ningun usuario.",negro)
        else:
            datosordenados = ordenar_json(datos)
            print("Lista de usuarios")
            for usuario in datosordenados:
                print("DNI: " + usuario["dni"] + ", Nombre: " + usuario["nombre"])   
    except:
        print(rojo,"No existe el archivo.",negro)

def leer_json(archivo):
    with open(archivo, "r") as f:
        datos = json.load(f)
    return datos  

def eliminar_usuario(archivo):
    dni = str(input("Introduce el dni para eliminar el usuario: "))
    dni = dni.upper() 

    datos = leer_json(archivo)
    encontrado = False
    contador = 0
    for usuario in datos:
        if usuario["dni"] == dni:
            del datos[contador]
            guardar_datos(archivo, datos)
            print(verde,"\nUsuario eliminado correctamente.",negro)   
            encontrado = True 
            break
        contador += 1
    
    if not encontrado:
        print(rojo,"\nUsuario no encontrado.",negro)
    
def modificar_usuario(archivo):
    dni = str(input("Introduce el dni para modificar: "))
    dni = dni.upper() 

    datos = leer_json(archivo)
    encontrado = False
    contador = 0
    for usuario in datos:
        if usuario["dni"] == dni:
            dni, nombre = recoger_datos(archivo)
            datos[contador]["dni"] = dni
            datos[contador]["nombre"] = nombre
            guardar_datos(archivo, datos)   
            print(verde,"\nUsuario modificado correctamente.",negro)   
            encontrado = True 
            break
        contador += 1

    if not encontrado:
        print(rojo,"\nUsuario no encontrado.",negro)

def comprobar_dni(dni):
    if len(dni) != 9:
        return True

    for i in range(0, 7):
        if not dni[i].isdigit():
            return True
        
    if dni[8].isdigit():
        return True

def guardar_datos(archivo, datos):
    with open(archivo, "w") as f: 
        json.dump(datos, f, indent=2)

def comprobar_nombre(nombre):
    if not nombre.isalpha():
        return True
   
    if len(nombre) < 3:
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