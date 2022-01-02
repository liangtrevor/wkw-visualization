from imdb import IMDb

ia = IMDb()

userIn = input("Enter a movie name. I'll return the director's results")



movie = ia.search_movie(userIn)
# theGrail is the object the rest of the code works with
# it gets the ID of the top result and puts the information in theGrail
theGrail = ia.get_movie(movie[0].movieID)
print("name of the movie: ", theGrail)
for i in theGrail['director']:
    for k in ia.search_person(str(i))[:1]:
        director = ia.get_person(k.personID)
        # print the movies directed by the director
        print("Movies directed by %s" % director)
        print ("-----------------")
        print("lil test -- what is director?:")
        print(director)
        # for movie_name in director['director movie']:
        #     print(movie_name)
