# grab film ratings to actors
import imdb
from imdb import IMDb
import pprint

ia = IMDb()


# returns a movie object
def movob(keyword):
    subResult = ia.search_movie(keyword)
    final = ia.get_movie(subResult[0].movieID)
    return final


# returns a director object
def getdirector(director):
    searchEm = ia.search_person(director)
    thePerson = searchEm[0]
    return thePerson


print(movob("in the mood for love"))

