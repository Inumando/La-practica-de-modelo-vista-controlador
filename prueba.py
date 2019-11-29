import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='armando', password = 'sql123', database='cinemex')
cursor = cnx.cursor()
query = ("SELECT * FROM user")
cursor.execute(query)
rows = cursor.fetchall()
print(rows)
cursor.close()
cnx.close()