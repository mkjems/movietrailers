#!/usr/bin/python2.7

# import the display functionality
import fresh_tomatoes


# Define a movie
class Movie:

    def __init__(self, title, posterUrl, youTubeTrailer):
        self.title = title
        self.poster_image_url = posterUrl
        self.trailer_youtube_url = youTubeTrailer

# Will hold movies to be shown
movies = []

# Create the movies to be shown
movies.append(Movie(
    "The Matrix",
    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8"
))

movies.append(Movie(
    "Inside Out",
    ("http://img2.wikia.nocookie.net/__cb20141002165753"
        "/pixar/images/5/5c/The-inside-out-poster.jpg"),
    "https://www.youtube.com/watch?v=WIDYqBMFzfg"
))

movies.append(Movie(
    "Before Midnight",
    ("https://fanart.tv/fanart/movies/132344/movieposter/"
        "before-midnight-52ca3211950d5.jpg"),
    "https://www.youtube.com/watch?v=euOJkb0U8vE"
))

# Display movies
fresh_tomatoes.open_movies_page(movies)
