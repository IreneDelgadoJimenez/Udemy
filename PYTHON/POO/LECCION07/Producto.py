def producto(param, param1):
    pass


class producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        producto.contador_productos += 1
        self._id_producto = producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f' Id producto {self._id_producto}, nombre:  {self._nombre}, precio: {self._precio}'

    if __name__ == '__main__':
        producto1 = producto('Camisa', 100.00)
        print(producto1)
        producto2 = producto('Pantalón',150.00)
        print(producto2)