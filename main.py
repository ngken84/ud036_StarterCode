import media
import fresh_tomatoes

shawshank = media.Movie("The Shawshank Redemption",
                        "The story of a man sent to Shawshank prison",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco",
                        "Sept. 23, 1994",
                        "Frank Darabont")
gump = media.Movie("Forrest Gump",
                   "The story of Forrest Gump",
                   "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                   "https://www.youtube.com/watch?v=uPIEn0M8su0",
                   "July 6, 1994",
                   "Robert Zemeckis")
walle = media.Movie("Wall-E",
                    "The earth has been ruined and all that is left is a lone trash cleaning robot.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                    "https://www.youtube.com/watch?v=8-_9n5DtKOc",
                    "June 27, 2008",
                    "Andrew Stanton")
kiki = media.Movie("Kiki's Delivery Service",
                   "Kiki is an apprentice witch trying to make it on her own in a new city",
                   "https://upload.wikimedia.org/wikipedia/en/0/07/Kiki's_Delivery_Service_(Movie).jpg",
                   "https://www.youtube.com/watch?v=4bG17OYs-GA",
                   "July 29, 1989",
                   "Hayao Miyazaki")

movies = [shawshank, gump, walle, kiki]

fresh_tomatoes.open_movies_page(movies)
