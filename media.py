import webbrowser

class Movie():
    def __init__(self, movie_title, released_year, duration, category, language, director, starring , movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.released_year = released_year
        self.category = category
        self.language = language
        self.director = director
        self.staring = starring
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
