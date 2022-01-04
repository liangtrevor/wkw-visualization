from collections import Counter
from data import actors, dictionary, filmsList
import pprint

cc = Counter()
pp = pprint.PrettyPrinter(indent=1)

recurring_actors = []

# TODO:
#  write a for loop that iterates through the actor list ten times
# TODO:
#  filter elements that do not occur more than once
#  make a lambda function that takes out most occuring element
# TODO:
#  store that element in a list called recurring_cast

# take out elements which only occur once
for i in actors:
    newActorList = list(filter(lambda s: actors.count(s) > 2, actors))
    newActorList = list(set(newActorList))

print(newActorList)

# remove actor duplicates from actors list

# TODO: filter dict data in data.py
#   compare each key:value pair to newActorList, and filter names
#   not in newActorList. then move onto next step below

# TODO: make a dataframe
#   rows: films
#   cols: actors
#   elements: role

for i in filmsList:
    dictionary[i] = list(filter(lambda s: s in newActorList, dictionary[i]))

pp.pprint(dictionary)

# then data will be put into tableau and connected