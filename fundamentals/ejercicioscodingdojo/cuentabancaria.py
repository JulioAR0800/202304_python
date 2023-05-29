class CuentaBancaria:
    def __init__(self, tasa_interes, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if self.balance >= monto:
            self.balance -= monto
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            interes_generado = self.balance * self.tasa_interes
            self.balance += interes_generado
        return self
    
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
    
CuentaBancaria.imprimir_todas_las_cuentas() 

CuentaBancaria(0.02).deposito(100).deposito(200).deposito(300).retiro(150).generar_interes().mostrar_info_cuenta()
CuentaBancaria(0.03).deposito(500).deposito(200).retiro(100).retiro(50).retiro(75).retiro(25).generar_interes().mostrar_info_cuenta()
