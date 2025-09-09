from empleado import Empleado

class Empleado_tiempo_completo(Empleado):
    def __init__(self, nombre: str, salario_base: float, bono: float):
        #super().__init__ = para referirse al constructor base
        super().__init__(nombre, salario_base)
        self.bono = bono
        
    def calcular_salario(self) -> float:
        return super().calcular_salario() + self.bono

if __name__ == '__main__':
    emp = Empleado_tiempo_completo('Bottger',1000,500)
    emp.mostrar_informacion()
    print(f'El salario de este mongol es: {emp.calcular_salario()}')