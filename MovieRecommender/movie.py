

class Movie:
    def __init__(self, json):
        self.title = json['title']
        self.overview = json['overview']
        self.genres = json['genre_ids']
        self.backdrop = json['backdrop_path']

