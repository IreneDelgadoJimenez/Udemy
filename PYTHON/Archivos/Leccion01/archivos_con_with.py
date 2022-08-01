from ManejoArchivos import ManejoArchivos

# with open('prueba.txt,'r', encoding='uft8') as archivo:
with ManejoArchivos('Prueba.txt') as archivo:
    print(archivo.read())
