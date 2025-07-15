from lib.database_connection import DatabaseConnection
from lib.movie import *

class MovieRepository():
    
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows =self.connection.execute('SELECT * FROM movies')
        movies = []
        for row in rows:
            item = Movie(row["id"], row["title"], row["release_year"], row["genre"])
            movies.append(item)
        return movies
    
    def find(self, id):
        rows = self.connection.execute('SELECT * FROM movies WHERE id = %s', [id])
        row = rows[0]
        return Movie(row["id"], row["title"], row["release_year"], row["genre"])
    
    def add(self, movie):
        self.connection.execute('INSERT INTO movies (title, release_year, genre) VALUES (%s, %s, %s)', [movie.title, movie.release_year, movie.genre])
        return None
    
    def delete(self, id):
        self.connection.execute('DELETE FROM movies WHERE id = %s', [id])
        return None