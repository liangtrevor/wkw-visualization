from imdb import IMDb
from imdb.Person import Person

# create an instance of the IMDb class
ia = IMDb()

movie = ia.search_movie('fallen angels 1995')
movie2 = ia.search_movie('chungking express')
movie3 = ia.search_movie('happy together 1997')
movie4 = ia.searh_movie('in the mood for love')
movie5 = ia.search_movie('days of being wild 1990')
movie6 = ia.search_movie('2046 2004')

# print(movie[0].movieID)

fa1995 = ia.get_movie(movie[0].movieID)
chungking = ia.get_movie(movie2[0].movieID)
hppytgt = ia.get_movie(movie3[0].movieID)
itmfl = ia.get_movie(movie4[0].movieID)
wild = ia.get_movie(movie5[0].movieID)
two046 = ia.get_movie(movie6[0].movieID)

nameDict = {}

#TODO: find a better way of doing this .. so memory heavy
#TODO: hmm maybe map filter reduce for
#TODO: generalize to any director
masterList = []
faList = []
chungList = []
hppyList = []
itmflList = []
wildList = []
two046List = []

for actor in fa1995['actors']:
    # print(actor['name'])
    # counter+=1
    # people = ia.search_person(actor['name'])
    faList.append(actor['name'])
    masterList.append(actor['name'])
    # print(people[0]['name'] + ': ' + people[0].personID)
    # if counter == len(itmfl['actors']):

# print("Chungking Express:")
for actor in chungking['actors']:
    theName = actor['name']
    masterList.append(theName)
    chungList.append(theName)

for actor in hppytgt['actors']:
    theName = actor['name']
    masterList.append(theName)
    hppyList.append(theName)

for actor in itmfl['actors']:
    theName = actor['name']
    masterList.append(theName)
    itmflList.append(theName)

for actor in wild['actors']:
    theName = actor['name']
    masterList.append(theName)
    wildList.append(theName)

for actor in two046['actors']:
    theName = actor['name']
    masterList.append(theName)
    two046List.append(theName)



# print("\nfalist:")
# print(falist)
# print("\nlist:")
# print(list)

# print(list)

# print("The common actors between Fallen Angels and Chungking Express are:")
# for i in faList:
#     if i in list:
#         print(i)
# for i in fa1995:
#     print(i)
    # if i in list:
    #     print(i)


# 3am implementation:
# 1. retrieve the names of all wkw actors
# 2. find out which 6-10 names appear the most
# 3. see which of those actors each wkw film featured and map them somehow

print('\ntest two')

print(Person.default_info)



# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])