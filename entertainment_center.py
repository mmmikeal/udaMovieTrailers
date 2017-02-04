import media
import fresh_tomatoes



# generate a series of Movie Objects that hold attributes:
# Movie title
# Movie Synopsis
# Movie poster
# Movie trailer


haramBae = media.Movie("Harambe was innocent", "A story of Harambe", "http://pixel.nymag.com/imgs/daily/selectall/2016/07/27/27-harambe-gorilla-heaven.w710.h473.2x.jpg", "https://www.youtube.com/watch?v=Py_1aCt2c0s")

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

boondocks = media.Movie("Boondock Saints", "Two brothers seek vengeance", "https://jmount43.files.wordpress.com/2012/03/936full-the-boondock-saints-poster.jpg", "https://www.youtube.com/watch?v=ydXojYfCF3I")

interstellar = media.Movie("Interstellar", "A rodeo in space", "http://cdn.collider.com/wp-content/uploads/interstellar-imax-poster.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw" )

starTrek = media.Movie("Star Trek", "A modern remake of the classic series",
  "https://timsfilmreviews.files.wordpress.com/2013/05/star-trek-poster.jpg", "https://www.youtube.com/watch?v=pKFUZ10Wmbw")

storks = media.Movie("Storks", "This bird works for Amazon","http://www.impawards.com/2016/posters/storks.jpg", " https://www.youtube.com/watch?v=ZENmkJk9fBM")

#Array of Movie Objects
moviesArray = [haramBae,avatar,boondocks, interstellar, starTrek, storks]

#freshTomatoes takes in an array input
fresh_tomatoes.open_movies_page(moviesArray)