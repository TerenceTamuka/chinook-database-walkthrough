import psycopg2

#connecting to our chinook database
connection = psycopg2.connect(database="chinook")

#building a cursor object insance of the database
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table
#cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only the "Name" column from the "Artist" table
cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 select only "Queen" from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
#cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ('Queen',))

#fetch the results (multiple)
#results = cursor.fetchall()

#fetch the results (single)
results = cursor.fetchone()

#close the connection
connection.close()

#print results
for result in results:
    print(result)