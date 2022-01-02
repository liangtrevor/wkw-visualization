# getting wkw films into excel wth Pandas and IMDbPY
from imdb import IMDb
import pprint
import pandas as pd

ia = IMDb()

director = ia.search_person('wong kar wai')

print(director)

print(director[0])

wkw = director[0]

print(wkw)

# printing cutely
pp = pprint.PrettyPrinter(indent = 4)

code = wkw.personID

# get wkw's info
wkw_results = ia.get_person_filmography(code)

wkwfilms_name = []
wkwfilms_verbose = []

for i in range(len(wkw_results['data']['filmography']['director'])):
    movie_name = wkw_results['data']['filmography']['director'][i]
    # wkwfilms.append(movie_name[0]['title'])
    # print(movie_name)
    # you don't need to specify int index in movie_name because
    # there is only a single movie returned, rather than a list of lists.
    wkwfilms_name.append(movie_name['title'])
    # this
    # wkwfilms_verbose.append(ia.get_movie(movie_name.movieID))
    # wkwfilms_verbose.append(ia.get_movie(movie_name.movieID))
    print(ia.get_movie(movie_name.movieID))
    # wkwfilms_verbose.append(movie_name.movieID)
print(wkwfilms_name)

# creating pandas dataframe with wkwfilms list
df = pd.DataFrame(wkwfilms_name)

# output the dataframe to excel
df.to_excel('wkw-filmography.xlsx', sheet_name = 'test')

# worst ranking implementation out there:
# 1. Pull all the actors from each movie and store their names in a
# dict with each value 0
# 2. see how many times each key pops up in list of actors
# - perhaps a 3D dictionary with which movie each person is in?
# 3. increment the proper key by 1 for every success
# 4. get top 10 key:value pairs and store in a list
# 5. make new pandas dataframe
# 6. put into excel

masterDict = {}

pp.pprint(wkwfilms_verbose)

# for i in wkwfilms_verbose:
    # masterDict[i['actors']] = 0

# pp.pprint(masterDict)