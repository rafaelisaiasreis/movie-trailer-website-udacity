import webbrowser


class Movie():
    """Classe Filmes, criada para ser usada com fresh_tomatoes
     para gerar a página HTML."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Construtor das variáveis da instância"""
        # Variáveis de instância que serão usadas
        # para criar a página HTML
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Rotina criada para mostrar os trailers"""
        webbrowser.open(self.trailer_youtube_url)
