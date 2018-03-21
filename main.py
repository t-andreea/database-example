import sqlite3

connection = sqlite3.connect('first_database.db')

c = connection.cursor()

c.execute('select name from test')

print(c.fetchall())

c.execute('insert into test (id, name, age) values (3, "AA", 32)')

c.execute('select * from test')

print(c.fetchall())

c.close()
connection.close()