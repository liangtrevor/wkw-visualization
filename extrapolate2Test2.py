# getting wkw films into excel wth Pandas and IMDbPY
from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent=4)
ia = IMDb()
ia2 = IMDb()

def getmovieObject(movie):
    film = ia.search_movie(movie)
    identity = ia.get_movie(film[0].movieID)
    # returns movie object
    return identity

def getDirector(director):
    searchEm = ia.search_person(director)
    thePerson = searchEm[0]
    return thePerson


wkw = (getDirector("wong kar wai")).personID

wkw_results = ia.get_person_filmography(wkw)

itemList = []

for i in range(len(wkw_results['data']['filmography']['director'])):
    current = getmovieObject(wkw_results['data']['filmography']['director'][i]['title'])
    # print(current['title'])
    # print(wkw_results['data']['filmography']['director'][i])
    itemList.append(current)
    print(current['actors'])

pp.pprint(itemList)

# director = ia.search_person('wong kar wai')
#
# wkw = director[0]
#
# code = wkw.personID
#
# # get wkw's info
# wkw_results = ia.get_person_filmography(code)
#
# wkwfilms_name = []
#
# wkwfilms_verbose = []
#
# movieThing = ia.get_movie('0096461')
#
# hppytest = wkw_results['data']['filmography']['director'][-8].movieID
#
# gettherightobject = ia.get_movie(hppytest)
#
# theList = []
#
# for i in range(len(wkw_results['data']['filmography']['director'])):
#     storeID = wkw_results['data']['filmography']['director'][i].movieID
#     # print(storeID)
#     # this should append the movie object from ID in the verbose list
#     wkwfilms_verbose.append(ia2.get_movie(storeID))
#
# # get one item from list:
#
# happy = wkwfilms_verbose[-8]
#
# print(happy['actors'])