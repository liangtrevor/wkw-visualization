from imdb import IMDb
from imdb.Person import Person
import pandas as pd
import pprint

pp = pprint.PrettyPrinter(indent = 1)

# create an instance of the IMDb class
ia = IMDb()

testlist = []

# search for movie
movie2 = ia.search_movie('happy together 1997')

# get first movie object result returned, grab its ID
hppy = ia.get_movie(movie2[0].movieID)
# hppy = movie2[0]

print(type(movie2[0]))

print(hppy)

testlist.append(hppy)

pp.pprint(hppy)

print(hppy['actors'])

for i in testlist:
    print("testlist test:")
    print(i['actors'])

nameDict = {}

print('chungking type:')
print(type(hppy))

#TODO: find a better way of doing this .. so memory heavy
#TODO: hmm maybe map filter reduce for
#TODO: generalize to any director
# masterList = []
# faList = []
# chungList = []
# hppyList = []
# itmflList = []
# wildList = []
# two046List = []