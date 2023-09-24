import gestorusuarios
import os

def ejecutar():
    os.system("cls")
    while True:
            print("\n- - - - - - - - - - - - - - - - - - - -")
            mostrar_menu()
            opcion = input("\nElija una opción: ")
            print("\n")

            if opcion == "1":
                gestorusuarios.mostrar_datos(archivo_json)
            
            elif opcion == "2":
                gestorusuarios.agregar_usuario(archivo_json)

            elif opcion == "3":
                gestorusuarios.modificar_usuario(archivo_json)

            elif opcion == "4":
                 gestorusuarios.eliminar_usuario(archivo_json)

            elif opcion == "5":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

def mostrar_menu():
    print("\n1. Mostrar todos los usuarios")
    print("2. Agregar usuario")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def crear_json(archivo):    
    if not os.path.exists(archivo):
        datos = []
        gestorusuarios.guardar_datos(archivo, datos)

if __name__ == "__main__":
    archivo_json = "usuarios.json"
    crear_json(archivo_json)
    ejecutar()


   

