from cuentabancaria import CuentaBancaria

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}

    def agregar_cuenta(self, tipo_cuenta, tasa_interes):
        self.cuentas[tipo_cuenta] = CuentaBancaria(tasa_interes)

    def hacer_deposito(self, monto, tipo_cuenta):
        if tipo_cuenta in self.cuentas:
            self.cuentas[tipo_cuenta].deposito(monto)
        else:
            print("Tipo de cuenta inválido")
        return self

    def hacer_retiro(self, monto, tipo_cuenta):
        if tipo_cuenta in self.cuentas:
            self.cuentas[tipo_cuenta].retiro(monto)
        else:
            print("Tipo de cuenta inválido")
        return self

    def mostrar_balance_usuario(self):
        for tipo_cuenta, cuenta in self.cuentas.items():
            balance = cuenta.mostrar_info_cuenta()
            print(f"{self.nombre}, {tipo_cuenta} balance: {balance}")
        return self


usuario = Usuario("John Doe")

usuario.agregar_cuenta("checking", 0.02)
usuario.agregar_cuenta("savings", 0.03)

usuario.hacer_deposito(100, "checking")
usuario.hacer_deposito(200, "checking")
usuario.hacer_retiro(150, "checking")
usuario.hacer_deposito(500, "savings")
usuario.hacer_retiro(100, "savings")

usuario.mostrar_balance_usuario()
