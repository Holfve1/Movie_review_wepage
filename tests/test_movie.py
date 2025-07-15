from lib.movie import *

def test_movie_initialises():
    movie = Movie(1, 'Jurrasic Park', 1993, 'sci-fi')
    assert movie.id == 1
    assert movie.title == 'Jurrasic Park'
    assert movie.release_year == 1993
    assert movie.genre == 'sci-fi'
