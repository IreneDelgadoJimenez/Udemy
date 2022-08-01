opcion = None
while opcion != 4:
    try:
    print('Opciones: ')
    print('1. Agregar Pelicula')
    print('2.Listar peliculas')
    print('3. Eliminar catalogo peliculas')
    print('4. Salir')
    opcion =int(input('Escribe tu opcion (1-4): '))

    if opcion == 1:
        nombre_pelicula = input('Proporciona el nombre de la pelicula: ')ç
        pelicula = Pelicula()
    execpt Exception as e:
    print(f'Ocurrio un error {e}')
    opcion = None
else:
    print('Salimos del programa')
