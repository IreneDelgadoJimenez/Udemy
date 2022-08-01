# Manejo de valores  infinitos
import math

infinito_positivo = float('inf')
print(f'infinito positivo: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito?: {math.isinf(infinito_negativo)}')