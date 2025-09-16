import unittest

class Profesional:
    def __init__(self, nombre: str, experiencia_años: int):
        self.nombre = nombre
        self.experiencia_años = experiencia_años

    def evaluar_desempeno(self):
        return 'Evaluación genérica de desempeño'

class Ingeniero(Profesional):
    def __init__(self, nombre: str, experiencia_años: int):
        super().__init__(nombre, experiencia_años)
        if self.experiencia_años < 1:
            self.experiencia_años = 1
    
    def evaluar_desempeno(self):
        if self.experiencia_años > 5:
            return f'Empleado: {self.nombre} \n Desempeño: Excelente \n Bono: 1000'
        else:
            if self.experiencia_años > 2:
                return f'Empleado: {self.nombre} \n Desempeño: Bueno \n Bono: 500'
            else:
                return f'Empleado: {self.nombre} \n Desempeño: Regular'
class Diseñador(Profesional):
    def __init__(self, nombre: str, experiencia_años: int):
        super().__init__(nombre, experiencia_años)
        if self.experiencia_años <  0:
            self.experiencia_años = 0
    
    def evaluar_desempeno(self):
        if self.experiencia_años > 7:
            return f'Empleado: {self.nombre} \n Desempeño: Excepcional \n Bono: 1500'
        else:
            if self.experiencia_años > 3:
                return f'Empleado: {self.nombre} \n Desempeño: Muy Bueno \n Bono: 750'
            else:
                if self.experiencia_años > 0:
                    return f'Empleado: {self.nombre} \n Desempeño: En desarrollo \n Bono: 200'
                else:
                    return f'Empleado: {self.nombre} \n Desempeño: Principiante'
    
class TestProfesional(unittest.TestCase):
    def setUp(self):
        # Ingenieros
        self.Ing1 = Ingeniero('Alejandro', 0)
        self.Ing2 = Ingeniero('Pedro', 6)
        self.Ing3 = Ingeniero('Jaime', 4)
        
        #Diseñadores
        self.Dis1 = Diseñador('Alekzandrov', 8)
        self.Dis2 = Diseñador('Maria', 5)
        self.Dis3 = Diseñador('Ariana', 2)
        self.Dis4 = Diseñador('Daniela', 0)
        
    def test_verifica_desempeño(self):
        self.assertEqual(self.Ing1.evaluar_desempeno(), 'Empleado: Alejandro \n Desempeño: Regular')
        self.assertEqual(self.Dis2.evaluar_desempeno(), 'Empleado: Maria \n Desempeño: Muy Bueno \n Bono: 750')
    
    def test_compara_experiencia(self):
        self.assertGreater(self.Dis1.experiencia_años, self.Ing2.experiencia_años)
        self.assertLess(self.Dis4.experiencia_años,self.Ing3.experiencia_años)
        
if __name__ == "__main__":
    unittest.main()