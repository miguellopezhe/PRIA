import json
import datetime
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
        else:
            break

    while True:
        if dni_repite(archivo,dni):
            print(rojo,"\nERROR: DNI repetido. Introduce los datos de nuevo.\n",negro)
            dni = str(input("Introduce el DNI: "))
        else:
            break

    nombre = str(input("Introduce el nombre: "))
    while True:
        if comprobar_nombre(nombre): 
            print(rojo,"\nERROR: Nombre incorrecto. Introduce los datos de nuevo.\n",negro)
            nombre = str(input("Introduce el nombre: "))
        else:       
            break  
    
    fecha = str(input("Introduce tu fecha de nacimiento (dd/MM/aaaa): "))
    while True:
        if comprobar_fecha(fecha): 
            print(rojo,"\nERROR: Fecha incorrecta. Introduce los datos de nuevo.\n",negro)
            fecha = str(input("Introduce tu fecha de nacimiento (dd/MM/aaaa): "))
        else:       
            break  

    dni = dni.upper() 
    nombre = nombre.capitalize()
    return dni, nombre, fecha

def agregar_usuario(archivo):

    dni, nombre, fecha = recoger_datos(archivo)

    usuario = Usuario(dni, nombre, fecha).to_json()    
  
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
                print("DNI: " + usuario["dni"] + ", Nombre: " + usuario["nombre"] + ", Fecha: " + usuario["fecha"])   
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
    dni = str(input("Introduce el dni de usuario para modificar sus datos: "))
    dni = dni.upper() 

    datos = leer_json(archivo)
    encontrado = False
    contador = 0
    for usuario in datos:
        if usuario["dni"] == dni:
            nombre, fecha = modificar_datos()
            datos[contador]["nombre"] = nombre
            datos[contador]["fecha"] = fecha
            guardar_datos(archivo, datos)   
            print(verde,"\nUsuario modificado correctamente.",negro)   
            encontrado = True 
            break
        contador += 1

    if not encontrado:
        print(rojo,"\nUsuario no encontrado.",negro)

def modificar_datos():

    respuesta = str(input("¿Quieres modificar el nombre? (S/N): "))
    while True:
        if respuesta == "S":
            nombre = str(input("Introduce el nombre: "))
            while True:
                if comprobar_nombre(nombre): 
                    print(rojo,"\nERROR: Nombre incorrecto. Introduce los datos de nuevo.\n",negro)
                    nombre = str(input("Introduce el nombre: "))
                else:
                    #coger el nombre del dni que ha metido      
                    break  
        elif respuesta == "N":
            break
        else:
            print("Respuesta incorrecta.")

    respuesta = str(input("¿Quieres modificar la fecha? (S/N): "))
    while True:
            if respuesta == "S":
                fecha = str(input("Introduce tu fecha de nacimiento (dd/MM/aaaa): "))
                while True:
                    if comprobar_fecha(fecha): 
                        print(rojo,"\nERROR: Fecha incorrecta. Introduce los datos de nuevo.\n",negro)
                        fecha = str(input("Introduce tu fecha de nacimiento (dd/MM/aaaa): "))
                    else:  
                        #coger el nombre del dni que ha metido      
                        break  
            elif respuesta == "N":
                break
            else:
                print("Respuesta incorrecta.")
 
    nombre = nombre.capitalize()
    return nombre, fecha

def comprobar_dni(dni):
    if len(dni) != 9:
        return True

    for i in range(0, 8):
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

def dni_repite(archivo, dni):
    datos = leer_json(archivo)
    
    dni = dni.upper()
    for usuario in datos:
        if usuario["dni"] == dni:
            return True
            
    return False

def ordenar_json(datos):
    return sorted(datos, key=lambda x: x["nombre"])

def calcular_edad(fecha):

    formato = fecha.split("/")

    dia = int(formato[0])
    mes = int(formato[1])
    año = int(formato[2])
    

    fecha_actual = datetime.date.today()
    fecha_nacimiento = datetime.date(año, mes, dia)

    diferencia = fecha_actual - fecha_nacimiento

    edad = diferencia.days // 365

    return edad

def comprobar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, "%d/%m/%Y")
    except:
        return True
    
    formato = fecha.split("/")

    dia = int(formato[0])
    mes = int(formato[1])
    año = int(formato[2])
    
    if dia < 1 or dia > 31:
        return False
   
    if mes < 1 or mes > 12:
        return False

    if 1900 < año < 2023:
        return False
    else:
        return True

def mostrar_edad(archivo):
    try:
        datos = leer_json(archivo) 
        if len(datos) == 0:
            print(rojo,"No hay ningun usuario.",negro)
        else:
            datosordenados = ordenar_json(datos)
            print("Lista de usuarios")
            for usuario in datosordenados:
                edad = str(calcular_edad(usuario["fecha"]))
                print("DNI: " + usuario["dni"] + ", Nombre: " + usuario["nombre"] + ", Fecha: " + usuario["fecha"] + ", Edad: " + edad)   
    except:
        print(rojo,"No existe el archivo.",negro)