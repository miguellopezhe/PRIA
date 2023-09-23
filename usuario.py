class Usuario:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
    
    def to_json(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
        }
