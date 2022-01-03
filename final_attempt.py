from imdb import IMDb
import pprint
from collections import Counter

cc = Counter()
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
filmNames = []
actors = []
filmsDict = {}

# if you need to pull id or names, etc -- manipulate this for loop
for i in filmsList:
    film = movob(i)
    # search for film and put object into filmObjects list
    filmObjects.append(film)
    # append film name to filmNames. formatted according to imdb
    filmNames.append(film['title'])

print("\n")

#TODO: get film:list pair by making for loops range(len(...))
# the intent of this is to get the current film

# iterate through filmObjects
for i in filmObjects:
    # templist will store actors of current movie
    tempList = []
    # iterate through current film's actors and append their string names to
    # tempList
    for k in i['actors']:
        # put all actors from current film into actors list
        currentNames = k['name']
        actors.append(currentNames)
        tempList.append(currentNames)
        # make key:value pair in filmsDict to create film to actor data structure
    currentFilm = i['title']
    filmsDict[currentFilm] = tempList
    # actors.append(i['actors'][0]['name'])

# just for testing
# print("actors:")
# print("-----")
# pp.pprint(actors)
#
# print("dictionary:")
# print("-----")
# pp.pprint(filmsDict)

# TODO:
#  write a for loop that iterates through the actor list ten times
# TODO:
#  make a lambda function that takes out most occuring element
# TODO:
#  store that element in a list called recurring_cast

# remove actor duplicates from actors list
