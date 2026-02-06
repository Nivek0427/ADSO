import uuid

class Autor:
    def __init__(self, nombre_completo, nacionalidad, fecha_nacimiento, biografia):
        self.id = str(uuid.uuid4())
        self.nombre_completo = nombre_completo
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.biografia = biografia

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre_completo}\n"
            f"Nacionalidad: {self.nacionalidad}\n"
            f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
            f"Biografía: {self.biografia}"
        )
    
    def get_nombre(self):
        return self.nombre_completo
    
    def set_nombre(self, nuevo_nombre):
        self.nombre_completo = nuevo_nombre

    def get_nacionalidad(self):
        return self.nacionalidad
    
    def set_nacionalidad(self, nueva_nacionalidad):
        self.nacionalidad = nueva_nacionalidad

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self, nueva_fecha_nacimiento):
        self.fecha_nacimiento = nueva_fecha_nacimiento

    def get_biografia(self):
        return self.biografia
    
    def set_biografia(self, nueva_biografia):
        self.biografia = nueva_biografia
    
