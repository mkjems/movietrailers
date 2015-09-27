"""Define a movie"""


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
