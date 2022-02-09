import sqlite3  #necessary packages imported

connection = sqlite3.connect('movies.db')   # connect method is responsible for creating the database
cursor = connection.cursor()

# insert query
insertQuery = "INSERT INTO adventurousMovies VALUES ('The Avengers', 'Robert Downey Jr.', 'Scarlett Johansson', 'Joe Russo', 2012)"

# execute method method is responsible for firing the query that we pass as a parameter
cursor.execute(insertQuery)
connection.commit()
