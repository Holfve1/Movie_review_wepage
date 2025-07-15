import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

from lib.movie_routes import apply_movie_routes
apply_movie_routes(app)


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
