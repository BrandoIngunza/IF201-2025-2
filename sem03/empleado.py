from abc import ABC, abstractmethod
#ABC = Permite gestionar clases abstractas. Abstract Base Clases
#Clase Abstracta = ?
# __init__ = Constructor de método para crear objetos
# self. = Para declarar atributo dentro de la clase
class Empleado(ABC):
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base
        
    def calcular_salario(self) -> float:
        return self.salario_base
    
    def mostrar_informacion(self):
        print(f'Empleado: {self.nombre} | Salario base: {self.salario_base}')
    
'''if "__name__" == "__main__":
    obj = Empleado('Juan', 1000)
    obj.mostrar_informacion()'''