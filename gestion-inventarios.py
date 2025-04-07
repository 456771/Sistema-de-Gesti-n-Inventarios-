from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Electronico(Producto):
    def __init__(self, nombre, precio, marca):
        super().__init__(nombre, precio)
        self.marca = marca

    def mostrar_informacion(self):
        print(f"Producto Electrónico: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Marca: {self.marca}")

class Alimento(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def mostrar_informacion(self):
        print(f"Producto Alimenticio: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Tipo: {self.tipo}")

producto_electronico = Electronico("Televisor", 500.0, "Samsung")
producto_alimento = Alimento("Manzana", 1.5, "Orgánico")

producto_electronico.mostrar_informacion()
print()  
producto_alimento.mostrar_informacion()