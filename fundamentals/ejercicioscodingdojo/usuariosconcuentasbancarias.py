from cuentabancaria import CuentaBancaria

class Usuario:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta

    def hacer_deposito(self, amount):
        self.cuenta.deposito(amount)
        return self

    def hacer_retiro(self, amount):
        self.cuenta.retiro(amount)
        return self

    def mostrar_balance_usuario(self):
        print(f"Balance del usuario {self.nombre}:")
        self.cuenta.mostrar_info_cuenta()
        return self


cuenta1 = CuentaBancaria(0.02)
usuario1 = Usuario("John Doe", cuenta1)
usuario1.hacer_deposito(100).hacer_deposito(200).hacer_retiro(50).mostrar_balance_usuario()
