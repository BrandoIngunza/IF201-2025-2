import unittest
class CuentaBancaria:
    def __init__(self, numero_cuenta: str, saldo: float):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    def Depositar(self, monto: float):
        self.saldo += monto
        
    def ConsultarSaldo(self):
        return f'Tu saldo es: {self.saldo}'
    
    def Retirar(self,monto: float,aplicar_cargo = False):
        if self.saldo > monto:
            return self.saldo - monto
        else:
            return 'Error' 
        
class CuentaAhorros(CuentaBancaria):
    def Retirar(self, monto: float, aplicar_cargo = False):
        if self.saldo <= 0:
            return 'Error'
        if aplicar_cargo == True and monto > 50:
            return self.saldo - (monto + 2)
        else:
            return self.saldo- monto
        
    def verificar_minimo_saldo(self, minimo: float):
        if self.saldo >= minimo:
            return True
        else:
            return False
        
class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, saldo: float, limite_diario = 1000):
        super().__init__(numero_cuenta, saldo)
        self.limite_diario = limite_diario
        
    def Retirar(self, monto: float, aplicar_cargo = False):
        self.limite_diario -= 1
        if self.limite_diario >= 0:
            if aplicar_cargo == True:
                return self.saldo - (monto*1.01)
            else:
                return self.saldo - monto
        else:
            return 'Operacion denegada, limite de retiro diario alcanzado'
    
    def Aplicar_interes_negativo(self, tasa: float):
        if tasa > 0:
           return self.saldo * ((100-tasa)/100) 

class TestProfesional(unittest.TestCase):
    def setUp(self):
        # CuentaAhorros
        self.Ahor1 = CuentaAhorros('1991125780', 5000)
        self.Ahor2 = CuentaAhorros('1991125000', 1000)
        
        #CuentaCorriente
        self.Corr1 = CuentaCorriente('109914570', 6000, 1)
        self.Corr2 = CuentaCorriente('108978512', 700, 2)
    
    def test_retirar_monto(self):
        
        self.assertEqual(self.Ahor1.Retirar(1000, False), 4000)
        self.assertEqual(self.Ahor2.Retirar(60,True), 938)
        self.assertEqual(self.Corr1.Retirar(1000,True), 4990)
        self.assertEqual(self.Corr2.Retirar(100,False), 600)
    
    def test_verificar_saldo(self):
        self.assertTrue(self.Ahor1.verificar_minimo_saldo(1100))
        self.assertFalse(self.Ahor2.verificar_minimo_saldo(1100))
    
    def test_Aplicar_interes(self):
        self.assertEqual(self.Corr1.Aplicar_interes_negativo(10),5400)
        self.assertEqual(self.Corr2.Aplicar_interes_negativo(10),630)
        
if __name__ == "__main__":
    unittest.main()