# definir una lista de tipo str
nombres =['Juan','Karla','Ricardo','María']
#imprimir la lista de nombres
print(nombres)
# acceder a lols elementos de una lista
print(nombres[0])
print(nombres[1])
# Acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#Imprimir un rango
print(nombres[0:2])
#Ir del inicio de la lista al indice (sin Incluirlo)
print(nombres[:3])
#Desde el indice indicado hasta el final
print(nombres[1:])
#Cambiar valor de la lista
nombres[3] = 'Ivone'
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No exixten más nombres en la lista')
    
