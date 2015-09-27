#!/usr/bin/python

"""Shows movie trailers in a browser"""

# import the display functionality
from fresh_tomatoes import open_movies_page


class Movie:
    """Define a movie"""

    # pylint: disable=too-few-public-methods
    def __init__(self, title, poster_image_url, trailer_youtube_url,
                 story_line):
        """Set the passed values on the object"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.story_line = story_line

# Will hold movies to be shown
MOVIES = []

# Create the movies to be shown
MOVIES.append(Movie(
    "The Matrix",
    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8",
    ("Neo (Keanu Reeves) believes that Morpheus (Laurence Fishburne),"
        " an elusive figure considered to be the most dangerous man alive,"
        " can answer his question -- What is the Matrix? Neo is contacted"
        " by Trinity (Carrie-Anne Moss), a beautiful stranger who leads him"
        " into an underworld where he meets Morpheus. They fight a brutal "
        "battle for their lives against a cadre of viciously intelligent "
        "secret agents. It is a truth that could cost Neo something more "
        "precious than his life")
))

MOVIES.append(Movie(
    "Inside Out",
    ("http://img2.wikia.nocookie.net/__cb20141002165753"
        "/pixar/images/5/5c/The-inside-out-poster.jpg"),
    "https://www.youtube.com/watch?v=WIDYqBMFzfg",
    ("Riley (Kaitlyn Dias) is a happy, hockey-loving 11-year-old Midwestern"
        " girl, but her world turns upside-down when she and her parents move"
        " to San Francisco. Riley's emotions -- led by Joy (Amy Poehler) -- "
        "try to guide her through this difficult, life-changing event. However"
        ", the stress of the move brings Sadness (Phyllis Smith) to the "
        "forefront. When Joy and Sadness are inadvertently swept into the far"
        " reaches of Riley's mind, the only emotions left in Headquarters are"
        " Anger, Fear and Disgust.")
))

MOVIES.append(Movie(
    "Before Midnight",
    ("https://fanart.tv/fanart/movies/132344/movieposter/"
        "before-midnight-52ca3211950d5.jpg"),
    "https://www.youtube.com/watch?v=euOJkb0U8vE",
    ("On the last night of their idyllic Greek vacation, longtime lovers Jesse"
        " (Ethan Hawke) and Celine (Julie Delpy) reminisce about their lives"
        " together and what different choices might have brought.")
))

# Display movies
open_movies_page(MOVIES)
