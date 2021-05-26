class Auto:
    def desplazamiento(self):
        print('Me desplazo usando 4 ruedas!!')
        
        
class Moto():
    
    def desplazamiento(self):
        print('Me desplazo en 2 ruedas!!')
        
class Camion():
    
    def desplazamiento(self):
        print('Me desplazo en 10 ruedas!!')
        

# moto = Moto()
# moto.desplazamiento()

# auto = Auto()
# auto.desplazamiento()

# camion = Camion()
# camion.desplazamiento()

def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()
    
mi_vehiculo = Moto()
desplazamiento_vehiculo(mi_vehiculo)