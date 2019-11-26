from .user import User
from .sala import Sala
from .movies import Movies
from .seats import Seats
from .billboard import Billboard
from .ticket import Ticket
from . import mvc_exceptions as m_e
import mysql.connector
from mysql.connector import errorcode
import datetime

class Model:
    def __init__(self):
        self.user = []
        cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinema')
        cursor = cnx.cursor()
    """
    ****************
    * User methods *
    ****************
    """
    def search_user(email):
        query=('SELECT email FROM users WHERE email = %s')
        self.cursor.execute(query, (email))


    def create_a_user(self, email, first_name, last_name, password):
        user = self.search_user(email)
