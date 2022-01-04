import pandas as pd
from imdb import IMDb
import pprint

# ============================================================================= #
# ====================== GLOBAL VARIABLE DECLARATIONS ========================= #
# ============================================================================= #
# wkw's top feature films
pp = pprint.PrettyPrinter(indent=1)
ia = IMDb()
filmsList = ['the grandmaster', '2046', 'eros', 'in the mood for love',
             'happy together 1997', 'fallen angels 1995', 'ashes of time',
             'chungking express', 'days of being wild', 'as tears go by']
filmObjects = []  # store film objects
filmNames = []  # store string names of films
actors = []  # store name of actors
filmsDict = {}  # store films in this dictionary for films:[actors] pairings later
actorToRole = {}  # store actor roles


# ============================================================================= #
# ====================== FUNCTIONS ========================= #
# ============================================================================= #

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


# if you need to pull id or names, etc -- manipulate this for loop
for i in filmsList:
    film = movob(i)
    # search for film and put object into filmObjects list
    filmObjects.append(film)
    # append film name to filmNames. formatted according to imdb
    filmNames.append(film['title'])

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

for i in actors:
    ActorList_twoOrMore = list(set(list(filter(lambda s: actors.count(s) >= 2, actors))))

# create a new list which contains actors who have appeared > 2 times

for i in actors:
    ActorList_moreThanTwo = list(set(list(filter(lambda s: actors.count(s) > 2, actors))))

pp.pprint(actors)

# remove actor duplicates from actors list

# TODO: make a dataframe
#   rows: films
#   cols: actors
#   elements: role

# # film: [actors] dict pair for actors who have appeared >= 2 times
filmsDict_twoOrMore = filmsDict
# # film: [actors] dict pair for actors who have appeared >= 2 times
filmsDict_moreThanTwo = filmsDict

for i in filmNames:
    filmsDict_twoOrMore[i] = list(filter(lambda s: s in ActorList_twoOrMore, filmsDict[i]))

for i in filmNames:
    filmsDict_moreThanTwo[i] = list(filter(lambda s: s in ActorList_moreThanTwo, filmsDict[i]))

pp.pprint(filmsDict)

# create dataframes
dictDf_twoOrMore = pd.DataFrame.from_dict(filmsDict_twoOrMore, orient='index')
dictDf_moreThanTwo = pd.DataFrame.from_dict(filmsDict_moreThanTwo, orient='index')

listDf_twoOrMore = pd.DataFrame(ActorList_twoOrMore)
listDf_moreThanTwo = pd.DataFrame(ActorList_moreThanTwo)

#
# converting data to .csv
#

# actors w/ 2 or more appearances
dictDf_twoOrMore.to_csv("./files/film-actors_two_or_more.csv")
# actors w/ more than 2 appearances
dictDf_moreThanTwo.to_csv("./files/film-actors_more_than_2.csv")

# actors w/ 2 or more appearances
listDf_twoOrMore.to_csv("./files/actors_two_or_more.csv")
# actors w/ 2 or more appearances
listDf_moreThanTwo.to_csv("./files/filesactors_more_than_2.csv")

# TODO: create dictionary of format:
#  film:actor:role
