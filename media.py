#!/usr/bin/python

"""Shows movie trailers in a browser"""

# import the display functionality and movies to display
from fresh_tomatoes import open_movies_page
from movies import MOVIES

# Display movies
open_movies_page(MOVIES)
