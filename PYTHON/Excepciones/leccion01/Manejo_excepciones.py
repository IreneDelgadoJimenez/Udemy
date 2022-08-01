from NumeroIdenticosException import NummerosIdenticosException
resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NummerosIdenticosException('números identicos')
    resultado = a/b
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')
except ZeroDivisionError as e:
    print(f' ZeroDivisionError - Ocurrió un error {e}', {type(e)})
except TypeError as e:
    print(f' TypeError - Ocurrió un error: {e}', {type(e)})

print(f'Resultado: {resultado}')
print('Continuamos...')