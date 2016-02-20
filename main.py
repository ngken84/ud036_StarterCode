import media
import fresh_tomatoes

# Define all my favorite movies, games and tv shows
shawshank = media.Movie(
    "The Shawshank Redemption",
    "The story of a man sent to Shawshank prison.",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=6hB3S9bIaco",  # noqa
    "Sept. 23, 1994",
    "Frank Darabont")

gump = media.Movie(
    "Forrest Gump",
    "The story of Forrest Gump.",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=uPIEn0M8su0",  # noqa
    "July 6, 1994",
    "Robert Zemeckis")

walle = media.Movie(
    "Wall-E",
    "The earth has been ruined and all that is left is "
    "a lone trash cleaning robot.",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",  # noqa
    "https://www.youtube.com/watch?v=8-_9n5DtKOc",  # noqa
    "June 27, 2008",
    "Andrew Stanton")

kiki = media.Movie(
    "Kiki's Delivery Service",
    "Kiki is an apprentice witch trying to make "
    "it on her own in a new city.",
    "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki's_Delivery_Service_(Movie).jpg",  # noqa
    "https://www.youtube.com/watch?v=4bG17OYs-GA",  # noqa
    "July 29, 1989",
    "Hayao Miyazaki")

chrono_trigger = media.VideoGame(
    "Chrono Trigger",
    "A group of adventurers use time "
    "travel to avert a worldwide disaster.",
    "http://www.videogameauctions.com/wp-content/uploads/2011/02/Chrono-Trigger-Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=vVl6Ue9r-Oo",  # noqa
    "March 11, 1995",
    "Squaresoft")

lastofus = media.VideoGame(
    "The Last of Us",
    "A man and a girl attempt to go across "
    "country during a zombie outbreak.",
    "http://mvpo.us/img/P4502",  # noqa
    "https://www.youtube.com/watch?v=W01L70IGBgE",  # noqa
    "June 14, 2013",
    "Naughty Dog")

destiny = media.VideoGame(
    "Destiny",
    "In the far distant future, Guardians protect the "
    "remnants of humanity from the threats "
    "from all corners of the universe.",
    "http://ecx.images-amazon.com/images/I/915Cy4YnGKL.jpg",  # noqa
    "https://www.youtube.com/watch?v=9ZyQK6kUdWQ",  # noqa
    "Sept. 15, 2014",
    "Bungie")

seinfeld = media.TelevisionShow(
    "Seinfeld",
    "A show about nothing.",
    "http://www.sonypictures.com/tv/seinfeld/assets/images/onesheet.jpg",  # noqa
    "https://www.youtube.com/watch?v=V-9WO6UG7rM",  # noqa
    "July 5, 1989",
    "NBC")

simpsons = media.TelevisionShow(
    "The Simpsons",
    "A cartoon disfunctional family goes on whacky adventures",
    "http://cdn.fontmeme.com/images/The-Simpsons-TV-Series.jpg",  # noqa
    "https://www.youtube.com/watch?v=nA4qEX6Cg2w",  # noqa
    "Dec. 17, 1989",
    "FOX")

# put them all in an array
movies = [shawshank, gump, walle, kiki, lastofus,
          chrono_trigger, destiny, seinfeld, simpsons]

# pass it to the open_movies_page function
fresh_tomatoes.open_movies_page(movies)
