from lib.database_connection import DatabaseConnection

def test_get_movie(db_connection, web_client):
    db_connection.seed('seeds/movie_reviews.sql')
    response = web_client.get('/movies')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Inception, The Dark Knight, Pulp Fiction, The Shawshank Redemption, Forrest Gump, Fight Club, The Matrix, The Lord of the Rings: The Fellowship of the Ring, Spirited Away, The Lord of the Rings: The Return of the King'

def test_post_movie(db_connection, web_client):
    db_connection.seed('seeds/movie_reviews.sql')
    response = web_client.post('/movies', data = {'title': '28 Years Later', 'release_year': 2025, 'genre': 'Horror'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Movie added successfully'