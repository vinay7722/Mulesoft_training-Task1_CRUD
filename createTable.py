import sqlite3  #necessary packages imported

connection = sqlite3.connect('movies.db')   # connect method is responsible for creating the database
cursor = connection.cursor()

# query to create table
createQuery = "CREATE TABLE IF NOT EXISTS adventurousMovies (name TEXT, actor TEXT, actress TEXT, director TEXT, yearOfRelease INTEGER)"

# execute method method is responsible for firing the query that we pass as a parameter
cursor.execute(createQuery)