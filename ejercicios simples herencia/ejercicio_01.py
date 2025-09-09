class Persona():
    def __init__(self, nombre: str,edad: int):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        return f'Hola, soy {self.nombre}, tengo {self.edad} añitos'

class Estudiante(Persona):
    def __init__(self, nombre:str, edad: int, carrera: str):
        super().__init__(nombre,edad)
        self.carrera = carrera

    def presentarse(self):
        return super().presentarse() + f' y estudio la carrera de {self.carrera}'
    
if __name__ == '__main__':
    ob = Estudiante('juan', 66, 'Ing.')
    print(ob.presentarse())