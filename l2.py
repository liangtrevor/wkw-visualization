from imdb import IMDb
from imdb.Person import Person
import pandas as pd

# create an instance of the IMDb class
ia = IMDb()

# this returns search results
movie = ia.search_movie('fallen angels 1995')
movie2 = ia.search_movie('chungking express')
movie3 = ia.search_movie('happy together 1997')
movie4 = ia.search_movie('in the mood for love')
movie5 = ia.search_movie('days of being wild 1990')
movie6 = ia.search_movie('2046 2004')

# print(movie[0].movieID)

fa1995 = ia.get_movie(movie[0].movieID)
chungking = ia.get_movie(movie2[0].movieID)
hppytgt = ia.get_movie(movie3[0].movieID)
itmfl = ia.get_movie(movie4[0].movieID)
wild = ia.get_movie(movie5[0].movieID)
two046 = ia.get_movie(movie6[0].movieID)

print("what you can do:")
print(ia.get_movie_infoset())

print("a result:")
# print(fa1995['plot'])
print(fa1995)