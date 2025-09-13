from collections.abc import Buffer
from unittest import result
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3080",
    database="odontologia_db"
)


cursor = db.cursor(buffered=True)

cursor.execute("SELECT * FROM users")

result = cursor.fetchall()


#cursor.execute("DELETE FROM users WHERE id = ")

print(result[0])


#cursor.execute("DELETE FROM users WHERE id = 3")
# db.commit()


cursor.execute("UPDATE users SET numeroID = '3133283876' WHERE id = 1")
print("Registros actualizados: ", cursor.rowcount)
db.commit()