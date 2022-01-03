import numpy as np
import pandas as pd
from final_attempt import movob
from imdb import IMDb
from data import updatedDict, filmsList
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
    # make a movie:object pair
    





# TODO: what we'll do:
#   for each dict value (actor), make it
#   attached to another dict.
#   this dict should be an actor:role pair.

for i in updatedDict:
    finalDict[i] = {z: movieObjects[i] \
                    for z in updatedDict[i]}

pp.pprint(finalDict)