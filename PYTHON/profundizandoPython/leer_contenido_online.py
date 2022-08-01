# leer contenido online
from urllib.request import urlopen

with urlopen('htpp://globalmentoring.com.mx/recursos/GlobalMetoring.txt') as mensaje:
   #  contenido = mensaje.read()
   contenido = mensaje.read().decode('utf8')
    print(contenido)

with open('nuevo_arvhivo.txt,'w', encoding='utf-8') as archivo:
    archivo.write(contenido)