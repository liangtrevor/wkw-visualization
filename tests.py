# format data for turning into pandas dataframe
# dataframe will be used for visualization
# tests.py file is testing a different approach from bambooNpandas.py

import numpy as np
import pandas as pd
from filter0 import movob
from imdb import IMDb
from data import updatedDict, filmsList, repeatActors
import pprint

ia = IMDb()

pp = pprint.PrettyPrinter(indent=1)

finalDict = {}

# come up w/ better name later
actorRole = {}

# get list of movie objects .. for roles
# should have got this earlier

# iterate through names of films

for i in filmsList:
    # put movie object of film into current
    current = movob(i)
    # store all actors in current into cast variable
    cast = current['actors']
    # populate actor:role dict by iterating over cast
    # actorRole dict pairs will look like actor: role
    for k in cast:
        #TODO: current problem: we are overwriting the dict every time.
        # if one of the names we care about is in repeatActors:
        if k['name'] in repeatActors:
            # print(k.currentRole['name'])
            # populate actorRole with actor's name : actor's role
            actorRole[k['name']] = k.currentRole['name']
            # quit()
            print("if statement reached. current state of actorRole:")
            print(actorRole)
        # actorRole[k]['name'] = k['name']
        # print("printing k:")
        # print(k['name'])
        # break

print("printing actorRole:")
print("-----")
pp.pprint(actorRole)

# should probably do in one for loop. oh well.
for i in filmsList:
    finalDict[i] = actorRole

print("-----")
print(":pray_emoji")
pp.pprint(finalDict)

# TODO: what we'll do:
#   for each dict value (actor), make it
#   attached to another dict.
#   this dict should be an actor:role pair.



# for i in updatedDict:
#     # finalDict is intended to be movie:actor:role
#     finalDict[i] = {z: actorRole[i] \
#                     for z in updatedDict[i]}

# for i in updatedDict:
#     finalDict[i] = {z: actor}
# for i in updatedDict:
#     print(actorRole[i])

# pp.pprint(finalDict)