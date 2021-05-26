class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.andando = True
        self.acelera = True
        self.frena = False

    def arrancar(self):
        self.andando = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nandando: {self.andando} \nacelerando: {self.acelera} \nfrena: {self.frena}')


class Furgon(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return 'El Furgon esta cargado\n'
        else:
            return 'El Furgon no esta cargado\n'


class Moto(Vehiculos):
    hcaballito = ''

    def caballito(self):
        self.hcaballito = 'voy haciendo caballito'

    def estado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nandando: {self.andando} \nacelerando: {self.acelera} \nfrena: {self.frena} \n y {self.hcaballito}')


class AElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarBateria(self):
        self.cargando = True


print('\n####### Moto #######\n')
miMoto = Moto('Yamaha', 'XT750')
miMoto.caballito()
miMoto.estado()

print('\n####### Furgon #######\n')

miFurgon = Furgon('Peugeot', 'Expert')
miFurgon.arrancar()
miFurgon.estado()
print(miFurgon.carga(True))


class BicicletasElectrica(AElectricos, Vehiculos):
    pass


miBici = BicicletasElectrica('Trek', 2021)