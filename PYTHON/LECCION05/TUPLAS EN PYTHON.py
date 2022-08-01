# Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
#Saber el largo
print(len(frutas))
#Acceder a un elemento
print(frutas[0])
#Navegación inversa
print(frutas[-1])
#Acceder a un rango de valores
print(frutas[0:1]) #Sin incluir el ultimo indice
#Recorrer elementos
for fruta in frutas:
    print(fruta, end=' ')
#Cambiar valor tupla
#frutas[0] = 'Pera'
frutasLista = list(frutas)
frutasLista[0] ='Pera'
frutas = tuple(frutasLista)
print('\n',frutas)
#emininar la tupla por completo
del frutas
print(frutas)






