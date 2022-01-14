import pandas as pd
from imdb import IMDb
import pprint

pp = pprint.PrettyPrinter(indent=1)
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


# wkw's top feature films
filmsList = ('the grandmaster', '2046', 'eros', 'in the mood for love',
             'happy together 1997', 'fallen angels 1995', 'ashes of time',
             'chungking express', 'days of being wild', 'as tears go by')

# store film objects
filmObjects = []
# store string names of films
filmNames = []
# store name of actors
actors = []
# store films in this dictionary for films:[actors] pairings later
filmsDict = {}
# store actor roles
actorToRole = {}

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
        actors.append(currentNames.strip())
        tempList.append(currentNames)
        # make key:value pair in filmsDict to create film to actor data structure
    currentFilm = i['title']
    filmsDict[currentFilm] = tempList

for i in actors:
    ActorList_twoOrMore = list(set(list(filter(lambda s: actors.count(s) >= 2, actors))))
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
    filmsDict_moreThanTwo[i] = list(filter(lambda s: s in ActorList_moreThanTwo, filmsDict[i]))

pp.pprint(filmsDict)

# create dataframes

dictDf_twoOrMore = pd.DataFrame.from_dict(filmsDict_twoOrMore, orient ='index')
dictDf_moreThanTwo = pd.DataFrame.from_dict(filmsDict_moreThanTwo, orient ='index')

listDf_twoOrMore = pd.DataFrame(ActorList_twoOrMore)
listDf_moreThanTwo = pd.DataFrame(ActorList_moreThanTwo)

filmName = pd.DataFrame(filmNames)

# converting data to .csv

# actors w/ 2 or more appearances
dictDf_twoOrMore.to_csv("./files/film-actors_two_or_more.csv")
# actors w/ more than 2 appearances
dictDf_moreThanTwo.to_csv("./files/film-actors_more_than_2.csv")

# actors w/ 2 or more appearances
listDf_twoOrMore.to_csv("./files/actors_two_or_more.csv")
# actors w/ 2 or more appearances
listDf_moreThanTwo.to_csv("./files/actors_more_than_2.csv")

# create .csv of analyzed movie names
filmName.to_csv("./files/film_names.csv")

fad = {}

# iterate over all film objects
for i in filmObjects:
    film = i['title']
    # store pairs in here
    tempActorDict = {}
    # tempRoleDict = {}
    for k in i['cast']:
        name = k['name']
        # check to see if it is the correct name
        if name in ActorList_twoOrMore:
            # print("Current Name: " + name)
            role = k.currentRole
            # create a dictionary of actor:role
            tempActorDict[name] = role
    # create a dictionary of film:actor:role
    pp.pprint(tempActorDict)
    fad[film] = tempActorDict

dictDf_fab = pd.DataFrame.from_dict(fad, orient ='index')

dictDf_fab.to_csv("./files/film-actor-role.csv")
