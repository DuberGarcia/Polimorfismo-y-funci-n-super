# Polimorfismo

# Definición -> Comportamientos diferentes 
# dependiendo de la clase hija que se esté usando

class Cuenta:
    def __init__(self, numero):
        if not numero.startswith(self.servicio):

            raise Exception("Servicio invalida.")
        
        self.numero = numero


class Ahorros(Cuenta):
    servicio = '003'

    def activar(self):
        print("Cuenta {} con Servicio 003 activado.".format(self.numero))


class Creditos(Cuenta):
    servicio = '004'

    def activar(self):
        print("Cuenta {} con Servicio 004 activado.".format(self.numero))

ahorros = Ahorros("0030002012")
ahorros.activar()

aportes = Ahorros("0010002012")
aportes.activar()

