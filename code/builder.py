#Builder - Constructor de usuarios

class Usuario:
    def __init__(self):
        self.nombre = None
        self.email = None
        self.edad = None
        self.suscripcion = None

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}")
        print(f"Email: {self.email}")
        if self.edad:
            print(f"Edad: {self.edad}")
        if self.suscripcion:
            print(f"Suscripción: {self.suscripcion}")


class UsuarioBuilder:
    def __init__(self):
        self.usuario = Usuario()

    def nombre(self, nombre):
        self.usuario.nombre = nombre
        return self

    def email(self, email):
        self.usuario.email = email
        return self

    def edad(self, edad):
        self.usuario.edad = edad
        return self

    def suscripcion(self, tipo):
        self.usuario.suscripcion = tipo
        return self

    def build(self):
        if not self.usuario.nombre or not self.usuario.email:
            raise ValueError("El nombre y el email son obligatorios")
        return self.usuario


# Ejemplo de uso
if __name__ == "__main__":
    usuario1 = (UsuarioBuilder()
                .nombre("Ana García")
                .email("ana@email.com")
                .build())

    usuario2 = (UsuarioBuilder()
                .nombre("Carlos Mendoza")
                .email("carlos@email.com")
                .edad(35)
                .suscripcion("Premium")
                .build())

    usuario1.mostrar_info()
    print("---")
    usuario2.mostrar_info()
