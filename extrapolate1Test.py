# getting wkw films into excel wth Pandas and IMDbPY



from imdb import IMDb
import pprint

pp = pprint.PrettyPrinter(indent=4)
ia = IMDb()

director = ia.search_person('wong kar wai')

wkw = director[0]

code = wkw.personID

# get wkw's info
wkw_results = ia.get_person_filmography(code)

wkwfilms_name = []

wkwfilms_verbose = []

# pp.pprint(wkw_results)

# for i in range(len(wkw_resuldts['data']['filmography']['director'])):
#     movie_name = wkw_results['data']['filmography']['director'][i]
#     wkwfilms_name.append(movie_name['title'])
#     wkwfilms_verbose.append(movie_name)

# for i in wkw_results['data']['filmography']['director']:
    # movieObject = ia.get_movie(i.movieiD)
    # movieThing = ia.get_movie('0096461')
    # movieThing = ia.get_movie(i.movieID)
    # wkwfilms_verbose.append(movieThing)

movieThing = ia.get_movie('0096461')

hppytest = wkw_results['data']['filmography']['director'][-8].movieID

gettherightobject = ia.get_movie(hppytest)

theList = []

for i in range(len(wkw_results['data']['filmography']['director'])):
    # print(i[counter])
    # counter+=1
    store = wkw_results['data']['filmography']['director'][i].movieID
    # theList.append(store)
    # store = wkw_results['data']['filmography']['director'][i]
    # theList.append(store['actors'])
    # test = (ia.get_movie(store))
    # theList.append(ia.get_movie(store))
    print(ia.get_movie(store))




# pp.pprint(theList)



# for i in theList:
#     print(i['actors'])

# pp.pprint(wkwfilms_verbose)

print('right object test:')
# print(gettherightobject['actors'])

# actors = []
#
# for i in wkwfilms_verbose:
#     print(i['actors'])



# print(wkwfilms_verbose[-8]['actors'])