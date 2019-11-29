import mysql.connector
from mysql.connector import errorcode

TABLES = {}
TABLES['user'] = (
    "CREATE TABLE `user` ("
    "   `email` varchar(25) NOT NULL,"
    "   `first_name` varchar(14) NOT NULL,"
    "   `last_name` varchar(15) NOT NULL,"
    "   `birthdate` date NOT NULL,"
    "   `password` varchar(20) NOT NULL,"
    "   PRIMARY KEY (`email`)"
    ") ENGINE=InnoDB"
)

TABLES['movies'] = (
    "CREATE TABLE `movies` ("
    "   `movie_name` varchar(35) UNIQUE NOT NULL,"
    "   `duration` int(4) NOT NULL,"
    "   `classification` varchar(4) NOT NULL,"
    "   `description` varchar(500) NOT NULL,"
    "   PRIMARY KEY (`movie_name`)"
    ") ENGINE=InnoDB"
)

TABLES['sala'] = (
    "CREATE TABLE `sala` ("
    "   `id_sala` int(4) NOT NULL AUTO_INCREMENT,"
    "   `sala_kind` varchar(15) NOT NULL,"
    "   `total_seat` int(4) NOT NULL,"
    "   PRIMARY KEY (`id_sala`)"
    ") ENGINE=InnoDB"
)

TABLES['billboard'] = (
    "CREATE TABLE `billboard` ("
    "   `show_id` int(5) NOT NULL AUTO_INCREMENT,"
    "   `movie_name` varchar(35) NOT NULL,"
    "   `id_sala` int(4) NOT NULL,"
    "   `date` date NOT NULL,"
    "   `hour` time NOT NULL,"
    "   `language` varchar(10),"
    "   PRIMARY KEY (`show_id`), KEY `movie_name` (`movie_name`),"
    "   KEY `id_sala` (`id_sala`),"
    "   CONSTRAINT billboard_obfk_1 FOREIGN KEY (`movie_name`)"
    "       REFERENCES `movies` (`movie_name`) ON DELETE CASCADE,"
    "   CONSTRAINT billboard_ibfk_2 FOREIGN KEY (`id_sala`)"
    "       REFERENCES `sala` (`id_sala`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

TABLES['ticket'] = (
    "CREATE TABLE `ticket` ("
    "   `transaction_id` int(20) NOT NULL AUTO_INCREMENT,"
    "   `show_id` int(5) NOT NULL,"
    "   `user_id` varchar(25) NOT NULL,"
    "   PRIMARY KEY (`transaction_id`), KEY `show_id` (`show_id`),"
    "   KEY `user_id` (`user_id`),"
    "   CONSTRAINT ticket_obfk_1 FOREIGN KEY (`show_id`)"
    "       REFERENCES `billboard` (`show_id`) ON DELETE CASCADE,"
    "   CONSTRAINT ticket_ibfk_2 FOREIGN KEY (`user_id`)"
    "       REFERENCES `user` (`email`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

DB_NAME = 'cinemex'
cnx = mysql.connector.connect(user='armando', password = 'sql123')
cursor = cnx.cursor()

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exist.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created succesfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()