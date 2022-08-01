from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creaccion Objeto Cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(5,'rojo')
print(f'Calculo área cuadrado: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creaccion Objeto rectangulo'.center(50,'-'))
rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'Calculo área rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)