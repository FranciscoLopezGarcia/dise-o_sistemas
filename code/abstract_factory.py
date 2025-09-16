#Abstract Factory - Familias de objetos para diferentes usuarios

from abc import ABC, abstractmethod


# Productos abstractos
class InterfazUI(ABC):
    @abstractmethod
    def mostrar_panel(self):
        pass

class MetodoEnvio(ABC):
    @abstractmethod
    def procesar_envio(self):
        pass


# Productos concretos (familia Admin)
class AdminUI(InterfazUI):
    def mostrar_panel(self):
        return "Panel de Administración"

class EnvioExpress(MetodoEnvio):
    def procesar_envio(self):
        return "Envío Express - 24 horas"


# Productos concretos (familia Usuario)
class UsuarioUI(InterfazUI):
    def mostrar_panel(self):
        return "Panel de Usuario"

class EnvioNormal(MetodoEnvio):
    def procesar_envio(self):
        return "Envío Normal - 3 a 5 días"


# Fábrica abstracta
class AbstractFactory(ABC):
    @abstractmethod
    def crear_interfaz(self):
        pass

    @abstractmethod
    def crear_metodo_envio(self):
        pass


# Fábricas concretas
class AdminFactory(AbstractFactory):
    def crear_interfaz(self):
        return AdminUI()

    def crear_metodo_envio(self):
        return EnvioExpress()


class UsuarioFactory(AbstractFactory):
    def crear_interfaz(self):
        return UsuarioUI()

    def crear_metodo_envio(self):
        return EnvioNormal()


# Cliente que usa la fábrica
class SistemaLibreria:
    def __init__(self, factory: AbstractFactory):
        self.ui = factory.crear_interfaz()
        self.envio = factory.crear_metodo_envio()

    def procesar_compra(self, libro):
        print(self.ui.mostrar_panel())
        print(self.envio.procesar_envio())
        print(f"Libro comprado: {libro}")


# Ejemplo de uso
if __name__ == "__main__":
    sistema_admin = SistemaLibreria(AdminFactory())
    sistema_admin.procesar_compra("Manual de Gestión")

    print("---")

    sistema_usuario = SistemaLibreria(UsuarioFactory())
    sistema_usuario.procesar_compra("El Hobbit")
