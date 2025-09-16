#Prototype - Clonación de Libros Prestados

import copy
from datetime import datetime, timedelta


class Prestamo:
    def __init__(self, libro, usuario, fechaInicio=None, fechaFin=None):
        self.libro = libro
        self.usuario = usuario
        self.fechaInicio = fechaInicio or datetime.now()
        self.fechaFin = fechaFin or (self.fechaInicio + timedelta(days=14))
        self.estado = "Activo"
        self.historial = ["Préstamo creado"]

    def clone_superf(self):
        return copy.copy(self)

    def clone_profu(self):
        return copy.deepcopy(self)

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        self.historial.append(f"Estado cambiado a {nuevo_estado}")

    def agregar_evento(self, evento):
        self.historial.append(evento)

    def mostrar_info(self):
        print(f"Libro: {self.libro}")
        print(f"Usuario: {self.usuario}")
        print(f"Estado: {self.estado}")
        print(f"Inicio: {self.fechaInicio.strftime('%d/%m/%Y')}")
        print(f"Fin: {self.fechaFin.strftime('%d/%m/%Y')}")
        print(f"Historial: {len(self.historial)} eventos")


# Ejemplo de uso
if __name__ == "__main__":
    original = Prestamo("El Quijote", "Juan Pérez")
    original.cambiar_estado("Extendido")

    # Clon superficial (comparte historial con el original)
    prestamo_superf = original.clone_superf()
    prestamo_superf.usuario = "María González"

    # Clon profundo (historial independiente)
    prestamo_profu = original.clone_profu()
    prestamo_profu.usuario = "Ana Martínez"
    prestamo_profu.cambiar_estado("Renovado")

    print("Prestamo Original:")
    original.mostrar_info()
    print(f"Comparte historial con shallow: {original.historial is prestamo_superf.historial}")

    print("\nPrestamo Deep Clone:")
    prestamo_profu.mostrar_info()
    print(f"Comparte historial con deep: {original.historial is prestamo_profu.historial}")
