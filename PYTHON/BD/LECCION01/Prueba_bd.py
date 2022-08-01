import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            llaves_primaria = ((1,2,3),)
            # id_persona = input('Proporciona el valor id_persona: ')
            cursor.execute(sentencia,llaves_primaria)
            cursor.execute(sentencia,)
            registros = cursor.fetchall()
            for registros in registros:
                print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
