print("proporciona los siguientes datos del libro: ")
nombre = input('proporciona el nombre del libro: ')
id = int(input('proporciona el ID del libro: '))
precio = float(input('proporciona el valor del libro: '))
envioGratuito = bool(input('Indica si es envio gratuito : '))

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto,debe escribir True/False"

print(f'''
    Nombre: {nombre}
    Id: {id}
    precio: {precio}
    envio Gratuito?: {envioGratuito}
''')
