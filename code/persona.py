#FINAL DISEÑO

class Persona():
    def __init__(self, nombre=None, apellido=None, edad=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    #GET
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    #SET
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_edad(self, edad):
        self.edad = edad

