import mysql.connector


database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3080",
    database="master_python"
)

cursor = database.cursor()



cursor.execute("""

CREATE TABLE IF NOT EXISTS cars(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modole varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_cars PRIMARY KEY(id)
)

""")

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

#cursor.execute("INSERT INTO cars (marca, modole, precio) VALUES ('Audi', 'A4', 20000)")

cars = [
    ("Audi", "A4", 20000),
    ("Audi", "A6", 25000),
    ("BMW", "M3", 30000),
    ("BMW", "M5", 40000),
    ("Mercedes", "C300", 28000),
]

# cursor.executemany("INSERT INTO cars (marca, modole, precio) VALUES (%s, %s, %s)", cars)

database.commit()

# cursor.execute("SELECT * FROM cars WHERE precio <= 40000 AND marca = 'BMW'")
result = cursor.fetchall()


for cars  in result:
    print(cars)

cursor.execute("SELECT * FROM cars")

cars  = cursor.fetchone()

print(cars)