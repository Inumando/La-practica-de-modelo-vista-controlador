from . import cinema_exceptions as c_e
import view.view import View
import mysql.connector
from mysql.connector import errorcode
import datetime

class Model:
    def __init__(self):
        self.user = []

    """
    ****************
    * User methods *
    ****************
    """
    def search_user(self, email):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT email FROM users WHERE email = %s')
        cursor.execute(query, (email))
        count = cursor.rowcount
        cursor.close()
        cnx.close()
        if count == 0:
            mail = 'no'
            return mail
        mail = email
        return mail

    def create_a_user(self, email, first_name, last_name, birthdate, password):
        idx = self.search_user(email)
        if idx == 'no':
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query = ('INSERT INTO user '
            '(email, first_name, last_name, birthdate, password) '
            'VALUES (%s, %s, %s, %s, %s)')
            data_query = (email, first_name, last_name, birthdate, password)
            cursor.execute(query, data_query)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            raise c_e.item_already_stored('A user with "{}" email already stored'.format(email.upper()))

    def read_all_users(self):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT * FROM users')
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    
    def read_a_user(self, email):
        idx = self.search_user(email)
        if idx != 'no':
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM users WHERE email = %s')
            cursor.execute(query, (idx))
            row = cursor.fetchone()
            cursor.close()
            cnx.close()
            return row
        else:
            raise c_e.item_not_stored('Can\'t read "{}" because it\'s not stored'.format(idx.upper()))
    
    def update_a_user(self, email, new_first_name, new_last_name, new_birthdate, new_password):
        idx = self.search_user(email)
        if idx != 'no':
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM users WHERE email = %s')
            cursor.execute(query, (idx))
            old_user = cursor.fetchone()
            data = 'SET '
            if new_first_name == '':
                new_first_name = old_user[1]
            else:
                data += 'first_name = '+ new_first_name + ', '
            if new_last_name == '':
                new_last_name = old_user[2]
            else:
                data += 'last_name = '+ new_last_name  + ', '
            if new_birthdate == '':
                new_birthdate = old_user[3]
            else:
                data += 'birthdate = '+ new_birthdate  + ', '
            if new_password == '':
                new_password == old_user[4]
            else:
                data += 'password = '+ new_password
            update = 'UPDATE users ' + data + ' WHERE email = %s'
            cursor.execute(update, (email))
            cursor.close()
            cnx.close()
            new_user = (email, new_first_name, new_last_name, new_birthdate, new_password)
        else:
            raise c_e.item_not_stored('Can\'t update "{}" because it\'s not stored'.format(email.upper()))
        return old_user, new_user
    
    def delete_a_user(self, email):
        try:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('DELETE * FROM users WHERE email = %s')
            cursor.execute(query, (email))
            cursor.close()
            cnx.close()
            self.view.display_user_deleted(email)
        except c_e.item_not_stored as e:
            self.view.item_not_stored_error(e)
    
    """
    ******************
    * Movies Methods *
    ******************
    """

    def search_movie(self, movie_name):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT movie_id FROM movies WHERE movie_name = %s')
        cursor.execute(query, (movie_name))
        idx = cursor.fetchone()
        cursor.close()
        cnx.close()
        if movie_name.lower() == idx.lower():
            return idx
        return 'none'

    def create_a_movie(self, movie_name, duration, classification, description):
        idx = self.search_user(movie_name)
        if idx == 'none':
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query = ('INSERT INTO movies '
            '(movie_name, duration, classification, description) '
            'VALUES (%s, %s, %s, %s)')
            data_query = (movie_name, duration, classification, description)
            cursor.execute(query, data_query)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            raise c_e.item_already_stored('The movie "{}" is already stored'.format(movie_name.upper()))

    def read_all_movies(self):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT * FROM movies')
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    
    def read_a_movie(self, movie_name):
        idx = self.search_user(movie_name)
        if idx != 'none':
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM movies WHERE movie_name = %s')
            cursor.execute(query, (idx))
            row = cursor.fetchone()
            cursor.close()
            cnx.close()
            return row
        else:
            raise c_e.item_not_stored('Can\'t read "{}" because it\'s not stored'.format(idx.upper()))
    
    def update_a_movie(self, old_movie_name, new_movie_name, new_duration, new_classification, new_description):
        idx = self.search_user(old_movie_name)
        if idx != 'none':
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM movies WHERE movie_name = %s')
            cursor.execute(query, (idx))
            old_movie = cursor.fetchone()
            data = 'SET '
            if new_movie_name == '':
                new_movie_name = old_movie[0]
            else:
                data += 'movie_name = '+ new_movie_name + ', '
            if new_duration == 0:
                new_duration = old_movie[1]
            else:
                data += 'duration = '+ str(new_duration)  + ', '
            if new_classification == '':
                new_classification = old_movie[2]
            else:
                data += 'classification = '+ new_classification  + ', '
            if new_description == '':
                new_password == old_user[3]
            else:
                data += 'description = '+ new_description
            update = 'UPDATE movies ' + data + ' WHERE movie_name = %s'
            cursor.execute(update, (old_movie_name))
            cursor.close()
            cnx.close()
            new_movie = (new_movie_name, new_duration, new_classification, new_description)
        else:
            raise c_e.item_not_stored('Can\'t update "{}" because it\'s not stored'.format(email.upper()))
        return old_movie, new_movie
    
    def delete_a_movie(self, movie_name):
        try:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('DELETE * FROM movies WHERE movie_name = %s')
            cursor.execute(query, (movie_name))
            cursor.close()
            cnx.close()
            self.view.display_movie_deleted(movie_name)
        except c_e.item_not_stored as e:
            self.view.item_not_stored_error(e)

    """
    *****************
    * Salas Methods *
    *****************
    """
    
    def search_sala(self, id_sala):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT id_sala FROM sala WHERE id_sala = %s')
        cursor.execute(query, (id_sala))
        idx = cursor.fetchone()
        count = cursor.rowcount()
        cursor.close()
        cnx.close()
        if count > 0:
            return idx
        return -1

    def create_a_sala(self, id_sala, sala_kind, total_seat):
        idx = self.search_user(id_sala)
        if idx < 0:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query = ('INSERT INTO sala '
            '(id_sala, sala_kind, total_seat) '
            'VALUES (%s, %s, %s)')
            data_query = (id_sala, sala_kind, total_seat)
            cursor.execute(query, data_query)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            raise c_e.item_already_stored('The sala "{}" is already stored'.format(id_sala.upper()))

    def read_all_salas(self):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT * FROM sala')
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    
    def read_a_sala(self, id_sala):
        idx = self.search_user(id_sala)
        if idx != -1:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM sala WHERE id_sala = %s')
            cursor.execute(query, (idx))
            row = cursor.fetchone()
            cursor.close()
            cnx.close()
            return row
        else:
            raise c_e.item_not_stored('Can\'t read sala "{}" because it\'s not stored'.format(idx))
    
    def update_a_sala(self, id_sala, new_sala_kind, new_total_seat):
        idx = self.search_user(id_sala)
        if idx != -1:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM sala WHERE id_sala = %s')
            cursor.execute(query, (idx))
            old_sala = cursor.fetchone()
            data = 'SET '
            if new_sala_kind == '':
                new_sala_kind = old_sala[1]
            else:
                data += 'sala_kind = '+ new_sala_kind + ', '
            if new_total_seat == 0:
                new_total_seat = old_sala[2]
            else:
                data += 'total_seat = '+ new_total_seat  + ' '
            update = 'UPDATE sala ' + data + ' WHERE id_sala = %s'
            cursor.execute(update, (id_sala))
            new_idx = cursor.lastrowid()
            cursor.close()
            cnx.close()
            new_sala = (new_idx, new_sala_kind, new_total_seat)
        else:
            raise c_e.item_not_stored('Can\'t update "{}" because it\'s not stored'.format(email.upper()))
        return old_sala, new_sala
    
    def delete_a_sala(self, id_sala):
        try:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('DELETE * FROM sala WHERE id_sala = %s')
            cursor.execute(query, (id_sala))
            cursor.close()
            cnx.close()
            self.view.display_sala_deleted(id_sala)
        except c_e.item_not_stored as e:
            self.view.item_not_stored_error(e)

"""
*********************
* Billboard Methods *
*********************
"""
    def search_show(self, movie_name, date, hour):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT show_id FROM billboard WHERE movie_name = %s AND date = %s and hour = %s')
        cursor.execute(query, (movie_name, date, hour))
        idx = cursor.fetchone()
        count = cursor.rowcount()
        cursor.close()
        cnx.close()
        if count > 0:
            return idx
        return -1
    
    def create_a_show(self, movie_name, id_sala, date, hour, language):
        idx = self.search_show(self, movie_name, date, hour)
        if idx < 0:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query = ('INSERT INTO billboard '
            '(movie_name, id_sala, date, hour, languaje) '
            'VALUES (%s, %s, %s, %s, %s)')
            data_query = (movie_name, id_sala, date, hour, language)
            cursor.execute(query, data_query)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            raise c_e.item_already_stored('The function of "{}" is already stored'.format(movie_name.upper()))
    
    def read_all_shows(self):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT * FROM billboard')
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    
    def read_a_show(self, movie_name, date, hour):
        idx = self.search_user(movie_name, date, hour)
        if idx > -1:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM billboard WHERE show_id = %s')
            cursor.execute(query, (idx))
            row = cursor.fetchone()
            cursor.close()
            cnx.close()
            return row
        else:
            raise c_e.item_not_stored('Can\'t read function of "{}" because it\'s not stored'.format(movie_name.upper()))

    def update_a_show(self, old_movie_name, new_movie_name, new_id_sala, old_date, new_date, old_hour, new_hour, new_languaje):
        idx = self.search_user(old_movie_name, old_date, old_hour)
        if idx != -1:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM billboard WHERE show_id = %s')
            cursor.execute(query, (idx))
            old_show = cursor.fetchone()
            data = 'SET '
            if new_movie_name == '':
                new_movie_name = old_show[1]
            else:
                data += 'movie_name = '+ new_movie_name + ', '
            if new_id_sala == 0:
                new_id_sala = old_show[2]
            else:
                data += 'id_sala = '+ str(new_id_sala)  + ', '
            if new_date == '':
                new_date = old_show[3]
            else:
                data += 'date = '+ new_date  + ', '
            if new_hour == '':
                new_hour = old_show[4]
            else:
                data += 'hour = '+ new_hour  + ', '
            if new_languaje == '':
                new_languaje = old_show[5]
            else:
                data += 'languaje = '+ new_languaje  + ' '
            update = 'UPDATE billboard ' + data + ' WHERE show_id = %s'
            cursor.execute(update, (idx))
            new_idx = cursor.lastrowid()
            cursor.close()
            cnx.close()
            new_show = (new_idx, new_movie_name, new_id_sala, new_date, new_hour, new_languaje)
        else:
            raise c_e.item_not_stored('Can\'t update "{}" because it\'s not stored'.format(email.upper()))
        return old_show, new_show
    
    def delete_a_show(self, movie_name, date, hour):
        idx = search_show(movie_name, date, hour)
        try:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('DELETE * FROM billboard WHERE show_id = %s')
            cursor.execute(query, (idx))
            cursor.close()
            cnx.close()
            self.view.display_sala_deleted(id_sala)
        except c_e.item_not_stored as e:
            self.view.item_not_stored_error(e)
    
    def movies_per_day(self, date):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT b.movie_name, m.classification, b.language FROM billboard b, movies m WHERE b.movie_name = m.movie_name AND date = %s')
        cursor.execute(query, date)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows

    def shows_per_day(self, movie_name, date):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT hour FROM billboard WHERE movie_name = %s AND date = %s')
        cursor.execute(query, (movie_name, date))
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
"""
******************
* Ticket Methods *
******************
"""

    def search_ticket(self, movie_name, date, hour, email):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT show_id FROM billboard WHERE movie_name = %s AND date = %s and hour = %s')
        cursor.execute(query, (movie_name, date, hour))
        show_id = cursor.fetchone()
        new_query('SELECT transaction_id FROM ticket WHERE show_id = %s AND user_id = %s')
        cursor.execute(new_query, (show_id, email))
        idx = cursor.fetchone()
        cursor.close()
        cnx.close()
        if count > 0:
            return idx
        return -1
    
    def create_a_ticket(self, movie_name, date, hour, email):
        idx = search_ticket(self, movie_name, date, hour, email)
        if idx < 0:
            show_id = self.search_show(self, movie_name, date, hour)
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query = ('INSERT INTO ticket '
            '(show_id, user_id) '
            'VALUES (%s, %s)')
            data_query = (show_id, email)
            cursor.execute(query, data_query)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            raise c_e.item_already_stored('The function of "{}" is already stored'.format(movie_name.upper()))
    
    def read_all_shows(self):
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
        query=('SELECT * FROM ticket')
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        cnx.close()
        return rows
    
    def read_a_show(self, movie_name, date, hour):
        idx = self.search_ticket(movie_name, date, hour)
        if idx > -1:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('SELECT * FROM ticket WHERE transaction_id = %s')
            cursor.execute(query, (idx))
            row = cursor.fetchone()
            cursor.close()
            cnx.close()
            return row
        else:
            raise c_e.item_not_stored('Can\'t read function of "{}" because it\'s not stored'.format(movie_name.upper()))
    
    def delete_a_show(self, movie_name, date, hour, email):
        idx = search_ticket(movie_name, date, hour, email)
        try:
            cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
            cursor = cnx.cursor()
            query=('DELETE * FROM ticket WHERE transaction_id = %s')
            cursor.execute(query, (idx))
            cursor.close()
            cnx.close()
            self.view.display_sala_deleted(id_sala)
        except c_e.item_not_stored as e:
            self.view.item_not_stored_error(e)
