from imdb import IMDb
ia = IMDb()

movie = ia.search_movie('fallen angels 1995')

print(movie)