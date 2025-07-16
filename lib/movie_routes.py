from lib.database_connection import get_flask_database_connection
from flask import Flask, request, render_template, redirect
from lib.movie import Movie
from lib.movie_repo import MovieRepository

def apply_movie_routes(app):
    # @app.route('/movies', methods = ['GET'])
    # def get_movie():
    #     connection = get_flask_database_connection(app)
    #     repository = MovieRepository(connection)
    #     movies = repository.all()
    #     return render_template('index.html', movies = movies)
    

    @app.route('/movies', methods = ['GET'])
    def get_movie():
        connection = get_flask_database_connection(app)
        repository = MovieRepository(connection)
        movies = repository.all()
        return render_template('test_index.html', movies = movies)
    
    @app.route('/movies', methods = ['POST'])
    def post_movie():
        connection = get_flask_database_connection(app)
        repository = MovieRepository(connection)
        movie = Movie(None, request.form ['title'], request.form ['release_year'], request.form ['genre'])
        movie = repository.add(movie)
        return 'Movie added successfully'
    
    