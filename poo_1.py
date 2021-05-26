class Carro:
    def __init__(self):
        self.__largo = 250
        self.__ancho = 130
        self.__ruedas = 4
        self.__andando = False
        
    def arrancar(self, arrancamos):
        self.__andando = arrancamos
        
        if self.__andando:
            revision = self.__informacion()            
        
        if self.__andando and revision:
            return 'El carro esta andando!'
        elif self.__andando and revision == False:
            return 'El carro esta fallando, revisar!!'
        else:
            return 'El carro esta estacionado!'
            
    def caracteristicas(self):
        print(f'El carro tiene {self.__ruedas} cauchos, un ancho de {self.__ancho} y un largo de {self.__largo}')
        
    def __informacion(self):
        print(f'Revisando el auto!!')
        
        self.gasolina = 'Ok'
        self.aceite = 'Ok'
        self.puertas = 'Cerradas'
        
        if self.gasolina == 'Ok' and self.aceite == 'Ok' and self.puertas == 'Cerradas':
            return True
        else:
            return False
        
        

miCarro1 = Carro()
print(miCarro1.arrancar(True))
miCarro1.caracteristicas()

print('\n########## segundo carro ##########\n')

miCarro2 = Carro()
print(miCarro2.arrancar(False))
miCarro2.caracteristicas()