class computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        computadora.contador_computadoras +=1
        self._id_computadora = Computadora.contador_computadoras
        self._mombre = nombre
        self._monitor = monitor
        self._telclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._mombre}: {self._id_computadora}
        monitor: {self._monitor}
        Teclado: {self._telclado}
        Raton: {self._raton} 
        '''

teclado1 = Teclado ('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP',15)
computadora1 = computadora('HP', monitor1, telcado1, raton1)
print(computadora1)