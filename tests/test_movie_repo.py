from lib.movie_repo import *
from lib.movie import *
from lib.database_connection import DatabaseConnection

def test_get_all(db_connection):
    db_connection.seed('seeds/movie_reviews.sql')
    repository = MovieRepository(db_connection)
    movies = repository.all()
    assert movies == [
        Movie(1, 'Inception', 2010,'Sci-fi'),
        Movie(2, 'The Dark Knight', 2008, 'Action'),
        Movie(3, 'Pulp Fiction', 1994,'Drama'),
        Movie(4, 'The Shawshank Redemption', 1994, 'Drama'),
        Movie(5, 'Forrest Gump', 1994, 'Drama'),
        Movie(6, 'Fight Club', 1999, 'Drama'),
        Movie(7, 'The Matrix', 1999, 'Sci-fi'),
        Movie(8, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 'Fantasy'),
        Movie(9, 'Spirited Away', 2001, 'Animation'),
        Movie(10, 'The Lord of the Rings: The Return of the King', 2003, 'Fantasy'),
    ]

def test_find_movie(db_connection):
    db_connection.seed('seeds/movie_reviews.sql')
    repository = MovieRepository(db_connection)
    movie = repository.find(1)
    assert movie == Movie(1, 'Inception', 2010,'Sci-fi')

def test_add_movie(db_connection):
    db_connection.seed('seeds/movie_reviews.sql')
    repository = MovieRepository(db_connection)
    repository.add(Movie(None, '28 Years Later', 2025, 'Horror'))
    movies = repository.all()
    assert movies == [
        Movie(1, 'Inception', 2010,'Sci-fi'),
        Movie(2, 'The Dark Knight', 2008, 'Action'),
        Movie(3, 'Pulp Fiction', 1994,'Drama'),
        Movie(4, 'The Shawshank Redemption', 1994, 'Drama'),
        Movie(5, 'Forrest Gump', 1994, 'Drama'),
        Movie(6, 'Fight Club', 1999, 'Drama'),
        Movie(7, 'The Matrix', 1999, 'Sci-fi'),
        Movie(8, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 'Fantasy'),
        Movie(9, 'Spirited Away', 2001, 'Animation'),
        Movie(10, 'The Lord of the Rings: The Return of the King', 2003, 'Fantasy'), 
        Movie(11, '28 Years Later', 2025, 'Horror'),  
    ]

def test_delete_movies(db_connection):
    db_connection.seed('seeds/movie_reviews.sql')
    repository = MovieRepository(db_connection)
    repository.delete(1)
    movies = repository.all()
    assert movies == [
        Movie(2, 'The Dark Knight', 2008, 'Action'),
        Movie(3, 'Pulp Fiction', 1994,'Drama'),
        Movie(4, 'The Shawshank Redemption', 1994, 'Drama'),
        Movie(5, 'Forrest Gump', 1994, 'Drama'),
        Movie(6, 'Fight Club', 1999, 'Drama'),
        Movie(7, 'The Matrix', 1999, 'Sci-fi'),
        Movie(8, 'The Lord of the Rings: The Fellowship of the Ring', 2001, 'Fantasy'),
        Movie(9, 'Spirited Away', 2001, 'Animation'),
        Movie(10, 'The Lord of the Rings: The Return of the King', 2003, 'Fantasy'),    
    ]

