def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Environment',PK='Primary Key' )
listarTerminos(DMBS='Database managemnt System')
