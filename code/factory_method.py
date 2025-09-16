#Factory Method - Creador de libros

from abc import ABC, abstractmethod


# Producto base
class Libro(ABC):
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass


# Productos concretos
class LibroFisico(Libro):
    def mostrar_info(self):
        return f"[Físico] {self.titulo} - {self.autor} - ${self.precio}"


class LibroDigital(Libro):
    def mostrar_info(self):
        return f"[Digital] {self.titulo} - {self.autor} - ${self.precio}"


# Creador base (fábrica)
class LogisticaLibro(ABC):
    @abstractmethod
    def crear_libro(self, titulo, autor, precio):
        pass


# Fábricas concretas
class LogisticaLibroFisico(LogisticaLibro):
    def crear_libro(self, titulo, autor, precio):
        return LibroFisico(titulo, autor, precio)


class LogisticaLibroDigital(LogisticaLibro):
    def crear_libro(self, titulo, autor, precio):
        return LibroDigital(titulo, autor, precio)


# Ejemplo de uso
if __name__ == "__main__":
    fabrica_fisica = LogisticaLibroFisico()
    fabrica_digital = LogisticaLibroDigital()

    libro1 = fabrica_fisica.crear_libro("El Quijote", "Cervantes", 25.99)
    libro2 = fabrica_digital.crear_libro("Clean Code", "Robert C. Martin", 35.99)

    print(libro1.mostrar_info())
    print(libro2.mostrar_info())
