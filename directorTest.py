# from imdb import IMDb
# ia = IMDb()
#
# movie = ia.get_movie('0816692')
# print("Name of the movie: ", movie)
# for i in movie['director']:
#     print("Director: ", i)
#     for k in ia.search_person(str(i))[:1]:
#         director = ia.get_person(k.personID)
#         print("Movies directed by %s" % director)
#         print("-------------------------------")
#         for movie_name in director['director movie']:
#             print(movie_name)



from imdb import IMDb
import pprint
ia = IMDb()
# 0112913
# this movie object is no mere string
movie = ia.get_movie('0112913')

pp = pprint.PrettyPrinter(indent = 4)

print(movie)

print(movie['director'])

# karwai is no mere string
karwai = movie['director']

code = karwai[0].personID

wkw_results = ia.get_person_filmography(code)

pp.pprint(wkw_results)

print(wkw_results)

# for i in range(len(wkw_results['data']['filmography']['director'])):
for i in range(100):
    print("\n")
    movie_name = wkw_results['data']['filmography']['director'][i]
    print(movie_name)

# movie = ia.get_movie('0816692')
# print("name of the movie: ", movie)
# for i in movie['director']:
#     print("Director: ", i)
#     director = ia.search_person(i["name"])
#     print(director)
