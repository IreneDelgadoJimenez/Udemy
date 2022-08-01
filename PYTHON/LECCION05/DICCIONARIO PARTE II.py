# dict (key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
# acceder a un elemento (key)
print(diccionario['IDE'])
# otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#modificando elementos
diccionario['IDE'] ='integrated development enviroment'
print(diccionario)
#Recorrer los elementos
for termino, valor in diccionario.items():
    print(diccionario,valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# comprobar existencia de algun elemento
print('IDE' in diccionario)

#Agregar un elemento
diccionario['PK'] ='Primary Key'
print(diccionario)

#Remover un elemento
diccionario.pop('DMBS')
print(diccionario)

#Limpiar
diccionario.clear()
print(diccionario)

#Eliminar el diccionario por completo
del diccionario
print(diccionario)
