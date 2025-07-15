class Movie:
    def __init__(self, id, title, release_year, genre):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.genre = genre
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Movie({self.id}, {self.title}, {self.release_year}, {self.genre})"