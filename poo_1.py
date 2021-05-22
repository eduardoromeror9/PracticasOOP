class Coche:
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enMarcha = False

	def arrancar(self):
		self.enMarcha = True

	def estado(self):
		if self.enMarcha:
			return 'La unidad esta andando!'
		else:
			return 'La unidad esta estacionada!'


miCoche = Coche()
print('El largo del auto es: ',miCoche.largoChasis)
print('El auto tiene : ',miCoche.ruedas,'ruedas!!')
# miCoche.arrancar()

print(miCoche.estado())