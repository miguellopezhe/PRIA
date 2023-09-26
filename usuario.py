class Usuario:
    def __init__(self):
        pass
    
    def __init__(self, dni, nombre, fecha):
        self.dni = dni
        self.nombre = nombre
        self.fecha = fecha
    
    def to_json(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "fecha": self.fecha,
        }

    def get_dni(self):  
        return self.dni
    
    def set_dni(self,dni):  
        self.dni=dni
    
    def get_nombre(self):  
        return self.nombre
    
    def set_nombre(self,nombre):  
        self.nombre=nombre

    def get_fecha(self):  
        return self.fecha
    
    def set_fecha(self,fecha):  
        self.fecha=fecha