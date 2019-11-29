import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinemex')
cursor = cnx.cursor()

"""
********************
* Llenado usuarios *
********************
"""
query = ('INSERT INTO user (email, first_name, last_name, birthdate, password) VALUES (%s, %s, %s, %s, %s)')
data_query = ('armando@gmail.com', 'Armando', 'Galvan', '1990-03-26', 'SRVA')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('brenda@gmail.com', 'Brenda', 'Paredez', '1995-05-15', 'cena')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('ian@gmail.com', 'Ian', 'Amstrong', '1989-07-17', 'fornais')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('marco@gmail.com', 'Marco', 'Rodriguez', '1991-11-01', 'saludos')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('paola@gmail.com', 'Paola', 'Rodriguez', '1997-10-18', 'relax')
cursor.execute(query, data_query)
cnx.commit()

"""
****************
* Llenado Sala *
****************
"""
query = ('INSERT INTO sala (sala_kind, '
'total_seat) VALUES (%s, %s)')
data_query = ('Imax', 54)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('4DX', 45)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Normal', 54)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('4DX', 45)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Normal', 54)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Imax', 54)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Normal', 54)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Normal', 54)
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Normal', 54)
cursor.execute(query, data_query)
cnx.commit()

"""
******************
* Llenado movies *
******************
"""
query = ('INSERT INTO movies (movie_name, duration, '
'classification, description) VALUES (%s, %s, %s, %s)')
data_insert = ('Star Wars', 120, 'AA', 'Guerra en las estrellas. ¿Skywalker se convertira en el proximo Jedi?')
cursor.execute(query, data_insert)
cnx.commit()

data_insert = ('Kung-fu Panda', 96, 'AA', 'Las aventuras del Panda Po para encontrarse consigo mismo')
cursor.execute(query, data_insert)
cnx.commit()

data_insert = ('Arrow', 110, 'B', 'Oliver Queen tras 5 años regresa de un naufragio listo para salvar a su ciudad del crimen')
cursor.execute(query, data_insert)
cnx.commit()

data_insert = ('The Flash', 115, 'A', 'Barry Allen obtiene poderes de velocidad tras caerle un rayo. ¿cómo utilizara sus poderes?')
cursor.execute(query, data_insert)
cnx.commit()

data_insert = ('Coco', 98, 'AA', 'Una pelicula inspirada en las hermosas tradiciones del día de muertos en México')
cursor.execute(query, data_insert)
cnx.commit()

data_insert = ('La maldición de las hermanas', 108, 'B15', 'Adaptandose a su madrastra nueva cosas raras comienzan a pasar alrededor de estar hemanas')
cursor.execute(query, data_insert)
cnx.commit()

"""
*********************
* Llenado Cartelera *
*********************
"""

query = ('INSERT INTO billboard (movie_name, id_sala, '
'date, hour, language) VALUES (%s, %s, %s, %s, %s)')

data_query = ('Star Wars', 5, '2019/11/28','16:25', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 6, '2019/11/28','15:45', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 2, '2019/11/28','17:50', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 5, '2019/11/28','18:40', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 6, '2019/11/28','17:55', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 2, '2019/11/28','20:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 5, '2019/11/28','21:00', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 6, '2019/11/28','20:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 2, '2019/11/29','15:30', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 5, '2019/11/29','16:25', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 6, '2019/11/29','15:45', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 2, '2019/11/29','17:50', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 5, '2019/11/29','18:40', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 6, '2019/11/29','17:55', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 2, '2019/11/29','20:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 5, '2019/11/29','21:00', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Star Wars', 6, '2019/11/29','20:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Kung-fu Panda', 1, '2019/11/28','15:00', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Kung-fu Panda', 1, '2019/11/28','16:55', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Kung-fu Panda', 1, '2019/11/28','18:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Kung-fu Panda', 1, '2019/11/29','15:00', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Kung-fu Panda', 1, '2019/11/29','16:55', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Kung-fu Panda', 1, '2019/11/29','18:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Arrow', 3, '2019/11/28','15:15', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Arrow', 3, '2019/11/28','17:25', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Arrow', 3, '2019/11/28','19:40', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Arrow', 3, '2019/11/29','15:15', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Arrow', 3, '2019/11/29','17:25', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Arrow', 3, '2019/11/29','19:40', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('The Flash', 4, '2019/11/28','15:15', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('The Flash', 7, '2019/11/28','17:25', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('The Flash', 4, '2019/11/28','19:40', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('The Flash', 4, '2019/11/29','16:15', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('The Flash', 7, '2019/11/29','18:25', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('The Flash', 4, '2019/11/29','20:40', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('La maldición de las hermanas', 8, '2019/11/28','15:10', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('La maldición de las hermanas', 9, '2019/11/28','16:45', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('La maldición de las hermanas', 9, '2019/11/28','18:55', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('La maldición de las hermanas', 8, '2019/11/29','16:10', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('La maldición de las hermanas', 9, '2019/11/29','17:45', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('La maldición de las hermanas', 9, '2019/11/29','19:55', 'Subtitled')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Coco', 8, '2019/11/28','19:55', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

data_query = ('Coco', 8, '2019/11/29','20:10', 'Doblada')
cursor.execute(query, data_query)
cnx.commit()

"""
******************
* Llenado Ticket *
******************
"""

query = ('INSERT INTO ticket (show_id, user_id) VALUES (%s, %s)')
data_query = (3, 'brenda@gmail.com')
cursor.execute(query, data_query)
cnx.commit()

data_query = (15, 'paola@gmail.com')
cursor.execute(query, data_query)
cnx.commit()

data_query = (23, 'armando@gmail.com')
cursor.execute(query, data_query)
cnx.commit()

data_query = (31, 'marco@gmail.com')
cursor.execute(query, data_query)
cnx.commit()

data_query = (37, 'armando@gmail.com')
cursor.execute(query, data_query)
cnx.commit()

cursor.close()
cnx.close()