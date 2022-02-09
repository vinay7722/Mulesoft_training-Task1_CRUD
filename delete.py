import sqlite3  #necessary packages imported

connection = sqlite3.connect('movies.db')   # connect method is responsible for creating the database
cursor = connection.cursor()

#delete query
deleteCommand = "DELETE FROM details WHERE name = 'test'"

# execute method method is responsible for firing the query that we pass as a parameter
cursor.execute(deleteCommand)
connection.commit()