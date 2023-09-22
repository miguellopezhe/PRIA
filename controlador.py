from modelo import GestorUsuarios
from vista import Vista

class Controlador:
    def __init__(self, archivo):
        self.gestor_usuarios = GestorUsuarios(archivo)
        self.vista = Vista()

    def ejecutar(self):
        self.gestor_usuarios.cargar_usuarios()


        while True:
            print("\n- - - - - - - - - - - - - - - - - - - -")
            self.vista.mostrar_menu()
            opcion = input("\nElija una opción: ")
            print("\n")

            if opcion == '1':
                usuarios = self.gestor_usuarios.obtener_todos_los_usuarios()
                self.vista.mostrar_usuarios(usuarios)
            elif opcion == '2':
                dni, nombre, apellido = self.vista.obtener_datos_usuario()
                self.gestor_usuarios.agregar_usuario(dni, nombre, apellido)
            elif opcion == '3':
                dni, nombre, apellido = self.vista.obtener_datos_usuario()
                self.gestor_usuarios.modificar_usuario(dni, nombre, apellido)
            elif opcion == '4':
                dni = input("Ingrese el DNI del usuario a eliminar: ")
                self.gestor_usuarios.eliminar_usuario(dni)
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    archivo_json = "usuarios.json"
    controlador = Controlador(archivo_json)
    controlador.ejecutar()