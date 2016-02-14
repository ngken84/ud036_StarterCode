class Media():
    def __init__(self, title, description, image, trailer_url, release_date):
        self.title = title
        self.description = description
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_url
        self.release_date

class Movie(Media):
    def __init__(self, title, description, image, trailer_url, release_date, director):
        Parent.__init__(self, title, description, image, trailer_url, release_date)
        self.director = director

    
        
        
