
class Diamante:
    def __init__(self,nombre, color,tamanio,precio):
        self.nombre = nombre
        self.color = color
        self.tamanio = tamanio
        self.precio = precio
    def __repr__(self):
        return "mi diamante tiene el nombre: " + str(self.nombre) + " y su color es: " + str(self.color) + " su tamaño es: " + str(self.tamanio) +  " su precio es: " + str(self.precio)


class Oro:
    def __init__ (self,nombre, kilates, precio, peso):
        self.nombre = nombre
        self.kilates = kilates
        self.precio = precio
        self.peso = peso
    def __repr__(self):
        return "mi oro tiene el nombre: " + str(self.nombre) + " y su kilate es: " + str(self.kilates) + " su precio es: " + str(self.precio) + " y su peso es: " + str(self.peso)


class Joyeria:
    def __init__(self,nombre, productosOro, productosDiamante):
        self.nombre = nombre
        self.productosOro = productosOro #esto va a recibir una lista
        self.productosDiamante = productosDiamante #aqui tambien vamos a recibir una lista
    def __repr__(self):
        return "mi joyeria es: " + str(self.nombre) + " tengo " + str(len(self.productosDiamante)) + " diamantes y tengo " + str(len(self.productosOro)) + " de oro"


def crearJoyeria():
        rojo = Diamante('rojo','rojo','500 gramos', 10)
        esmeralda = Diamante('esmeralda','verde','1 kilo', 500)
        fenix = Diamante('fenix','naranja','1 tonelada', 1000)

        catorce = Oro('14 kilates',14,500,'10 gramos')
        blanco = Oro('blanco',20,1000,'50 gramos')


        diamantes = []
        diamantes.append(rojo)
        diamantes.append(esmeralda)
        diamantes.append(fenix)

        oros = []
        oros.append(catorce)
        oros.append(blanco)

        joyeria = Joyeria('Pampita', oros,diamantes)

        return joyeria



def imprimirJoyeria():

    joyeriaPampita = crearJoyeria()
    print(joyeriaPampita)



print(imprimirJoyeria())

        




