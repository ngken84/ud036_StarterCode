import re

class Media():
    tile_content = '''
        <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
            <h2>{movie_title}</h2>
            <h3>Released: {release_date}</h3>
            <div>{body}</div>
        </div>
    '''
    
    def __init__(self, title, description, image, trailer_url, release_date):
        self.title = title
        self.description = description
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        self.release_date = release_date

    def getYouTubeId(self):
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_youtube_url)
        return (youtube_id_match.group(0) if youtube_id_match
                              else None)

    def getTileContent(self):
        trailer_youtube_id = self.getYouTubeId()
        return Media.tile_content.format(
            movie_title = self.title,
            poster_image_url = self.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            release_date = self.release_date,
            body = self.description)
            

class Movie(Media):
    def __init__(self, title, description, image, trailer_url, release_date, director):
        Media.__init__(self, title, description, image, trailer_url, release_date)
        self.director = director

    def getTileContent(self):
        trailer_youtube_id = self.getYouTubeId()
        description = self.description + " Directed by " + self.director + "."
        return Media.tile_content.format(
            movie_title = self.title,
            poster_image_url = self.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            release_date = self.release_date,
            body = description)


class VideoGame(Media):
    def __init__(self, title, description, image, trailer_url, release_date, developer):
        Media.__init__(self, title, description, image, trailer_url, release_date)
        self.developer = developer

    def getTileContent(self):
        trailer_youtube_id = self.getYouTubeId()
        description = self.description + " Developed by " + self.developer + "."
        return Media.tile_content.format(
            movie_title = self.title,
            poster_image_url = self.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            release_date = self.release_date,
            body = description)

class TelevisionShow(Media):
    def __init__(self, title, description, image, trailer_url, release_date, network):
        Media.__init__(self, title, description, image, trailer_url, release_date)
        self.network = network

    def getTileContent(self):
        trailer_youtube_id = self.getYouTubeId()
        description = self.description + " Aired on " + self.network + "."
        return Media.tile_content.format(
            movie_title = self.title,
            poster_image_url = self.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            release_date = self.release_date,
            body = description)
        


        
