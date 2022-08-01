# set
planetas = {'Marte','Jupiter','Venus'}
print(planetas)
#largo de los elementos
print(len(planetas))
# revisar si un elemento esta presente
print('Marte' in planetas)
# Agregar más elementos
planetas.add('Tierra')
print(planetas)
#No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
#Eliminar elementos posoblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
#Eliminar elementos sin arrojar error
planetas.discard('Jupiter')
print(planetas)
#Eliminar set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
print(planetas)
