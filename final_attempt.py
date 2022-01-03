from imdb import IMDb
import pprint
from typing import List

pp = pprint.PrettyPrinter(indent=1)

ia = IMDb()


def movob(keyword):
    subResult = ia.search_movie(keyword)
    final = ia.get_movie(subResult[0].movieID)
    return final


# returns a director object
def getdirector(director):
    searchEm = ia.search_person(director)
    thePerson = searchEm[0]
    return thePerson

filmsList = ['the grandmaster', '2046', 'eros', 'in the mood for love',
        'happy together 1997', 'fallen angels 1995', 'ashes of time',
        'chungking express', 'days of being wild', 'as tears go by']

filmObjects = []
actors = []
filmsDict = {}

for i in filmsList:
    # search for film and put object into filmObjects list
    filmObjects.append(movob(i))

print("\n")

#TODO: get film:list pair by making for loops range(len(...))
# the intent of this is to get the current film

quit()

# iterate through filmObjects
for i in filmObjects:
    # templist will store actors of current movie
    tempList = []
    # iterate through current film's actors and append their string names to
    # tempList
    for k in i['actors']:
        # put all actors from current film into actors list
        actors.append(k['name'])
        # make key:value pair in filmsDict to create film to actor data structure
    currentFilm = i['title']
    filmsDict[currentFilm] = tempList
    # actors.append(i['actors'][0]['name'])

print("actors:")
print("-----")
pp.pprint(actors)

print("dictionary:")
print("-----")
pp.pprint(filmsDict)
