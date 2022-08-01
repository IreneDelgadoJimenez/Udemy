from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones = 0


    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.if_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self.if_raton}, Marca: {self._marca}, Tipo_entrada: {self._tipo_entrada}'
raton = Raton1('HP', 'USB')
print(raton1)


