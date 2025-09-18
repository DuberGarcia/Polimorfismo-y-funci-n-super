# Función super()

# Definición: super() permite llamar métodos y acceder a propiedades 
# de la clase base desde una subclase.

from abc import ABC, abstractmethod

class Cuenta(ABC):
    def __init__(self, numero, es_activo):
        self.numero = numero
        self.activo = es_activo

    @abstractmethod
    def calcular_interes_mensual(self):
        tasa_base = 0.001  # 0.1% mensual
        print(f"Tasa base aplicada: {tasa_base}")
        return tasa_base


class Ahorros(Cuenta):
    def __init__(self, numero, es_activo, saldo):
        super().__init__(numero, es_activo)
        self.saldo = saldo

    def calcular_interes_mensual(self):
        valor_base = super().calcular_interes_mensual()
        return valor_base


class Creditos(Cuenta):
    def __init__(self, numero, es_activo, saldo, plazo, tasa):
        super().__init__(numero, es_activo)
        self.saldo = saldo
        self.plazo = plazo
        self.tasa = tasa

    def calcular_interes_mensual(self):
        valor_base = super().calcular_interes_mensual()
        interes_credito = self.saldo * self.tasa
        return valor_base + interes_credito


class CDAT(Cuenta):
    def __init__(self, numero, es_activo, saldo, plazo, tasa, monto):
        super().__init__(numero, es_activo)
        self.saldo = saldo
        self.plazo = plazo
        self.monto = monto
        self.tasa = tasa

    def calcular_interes_mensual(self):
        valor_base = super().calcular_interes_mensual()
        calculo_cdat = self.saldo + self.tasa
        return valor_base + calculo_cdat

ahorro = Ahorros("001", True, 12.00)
credito = Creditos("004", True, 4000.00, 12, 1.5)
cdat = CDAT("004", True, 4000.00, 12, 1.5, 0.00)

print(credito.numero)
print(credito.activo)
print(credito.saldo)

print(credito.calcular_interes_mensual())
print(cdat.calcular_interes_mensual())
print(ahorro.calcular_interes_mensual())

