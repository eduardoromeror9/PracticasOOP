class Persona:
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia
        
    def descripcion(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad} \nResidencia: {self.residencia}')


class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self):
        super().descripcion()
        print(f'Salario: {self.salario} \nAntiguedad: {self.antiguedad}')
        
manuel = Empleado(3500, 5, 'Eduardo', 34, 'Chile\n')
manuel.descripcion()

comprobar = isinstance(manuel, Empleado)
print('Manuel pertenece a la instancia Empleado?: ', comprobar)