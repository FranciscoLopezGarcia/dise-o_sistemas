#Singleton - BD unica (thread-safe + lazy initialization)

import threading

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Database, cls).__new__(cls)
                    cls._instance.libros = []
        return cls._instance

    def agregar_libro(self, titulo, autor):
        libro = {"titulo": titulo, "autor": autor, "id": len(self.libros) + 1}
        self.libros.append(libro)

    def lista_libros(self):
        for libro in self.libros:
            print(f"{libro['id']}. {libro['titulo']} - {libro['autor']}")

    def get_total_libros(self):
        return len(self.libros)



# Ejemplo de uso
if __name__ == "__main__":
    db1 = Database()
    db1.agregar_libro("1984", "George Orwell")
    db1.agregar_libro("El Quijote", "Cervantes")

    db2 = Database()  # Mismo objeto que db1
    db2.agregar_libro("El Principito", "Saint-Exupery")

    print("DB1 libros:")
    db1.lista_libros()
    print(f"Son la misma instancia: {db1 is db2}")
