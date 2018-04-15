class Movie ():
    """ This class is used to store info about about a movie

    Arguments:
        movie_title(str): The second parameter is a string -
        movie title.
        Extracted from the json object which return after making a call to API

        poster_image_url(str): The third parameter -
        url for the movie's poster image.
        Extracted from the json object which return after making a call to API

        movie_overview(str): The fourth parameter - a string consisting
        of short description of the movie. Extracted from the json object
        which return after making a call to API

        trailer_youtube_id(str): The fifth parameter -
        a string, id of movie's trailer

        trailer_youtube_url(str): The sixth parameter -
        url for the movie's trailer on youtube
    """

    def __init__(
            self,
            movie_title,
            poster_image_url,
            movie_overview,
            trailer_youtube_id,
            trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.overview = movie_overview
        self.trailer_youtube_id = trailer_youtube_id
        self.trailer_youtube_url = trailer_youtube_url
