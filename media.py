import re


class Media():
    """ This class describes a media object like a
    movie, tv show or videogame. 
    """
    
    tile_content = '''
        <div class="col-md-6 col-lg-4 movie-tile text-center"
                data-trailer-youtube-id="{trailer_youtube_id}"
                data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h2>{movie_title}</h2>
            <h3>Released: {release_date}</h3>
            <div>{body}</div>
        </div>
    '''

    def __init__(self, title, description, image, trailer_url, release_date):
        """ Constructor for Media object.
        title - (String) the media's title
        description - (String) a description
        image - (String) a link to an image for the media
        trailer_url - (String) a link to the youtube trailer
        release_date - (String) release date of the media
        """
        self.title = title
        self.description = description
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        self.release_date = release_date

    def getYouTubeId(self):
        """ returns the id for the media's youtube trailer
        """
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        return (youtube_id_match.group(0) if youtube_id_match else None)

    def getTileContent(self):
        """ uses the tile content template to create a html div for the media
        object
        """
        trailer_youtube_id = self.getYouTubeId()
        description = self.getDescription()
        return Media.tile_content.format(
            movie_title=self.title,
            poster_image_url=self.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_date=self.release_date,
            body=description)

    # get the description of the media object
    def getDescription(self):
        """ returns the description
        """
        return self.description


class Movie(Media):
    """ This class describes a movie adding a director
    parameter to the Media object
    """
    
    def __init__(self, title, description, image,
                 trailer_url, release_date, director):
        """ Constructor for Movie object.
        title - (String) the media's title
        description - (String) a description
        image - (String) a link to an image for the media
        trailer_url - (String) a link to the youtube trailer
        release_date - (String) release date of the media
        director - (String) director of the movie
        """
        Media.__init__(self, title, description,
                       image, trailer_url, release_date)
        self.director = director

    def getDescription(self):
        """ returns the description adds a 'Directed by'
        statement at the end of the description
        """
        return self.description + " Directed by " + self.director + "."


class VideoGame(Media):
    """ This class describes a videogame adding a developer
    parameter to the Media object
    """
    
    def __init__(self, title, description, image,
                 trailer_url, release_date, developer):
        """ Constructor for VideoGame object.
        title - (String) the media's title
        description - (String) a description
        image - (String) a link to an image for the media
        trailer_url - (String) a link to the youtube trailer
        release_date - (String) release date of the media
        developer - (String) developer of the game
        """
        Media.__init__(self, title, description,
                       image, trailer_url, release_date)
        self.developer = developer

    def getDescription(self):
        """ returns the description adds a 'Developed by'
        statement at the end of the description
        """
        return self.description + " Developed by " + self.developer + "."


class TelevisionShow(Media):
    """ This class describes a television adding a network
    parameter to the Media object
    """
    
    def __init__(self, title, description,
                 image, trailer_url, release_date, network):
        """ Constructor for TelevisionShow object.
        title - (String) the media's title
        description - (String) a description
        image - (String) a link to an image for the media
        trailer_url - (String) a link to the youtube trailer
        release_date - (String) release date of the media
        network - (String) the network the show aired on
        """
        Media.__init__(self, title, description,
                       image, trailer_url, release_date)
        self.network = network

    def getDescription(self):
        """ returns the description adds a 'Aired on'
        statement at the end of the description
        """
        return self.description + " Aired on " + self.network + "."
