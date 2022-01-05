import matplotlib as pl
import numpy as np
import pandas as pd
import csv

actorList = []
filmsList = []

df_actorsMoreThanTwo = pd.read_csv("./files/actors_more_than_2.csv")

df_filmsMoreThanTwo = pd.read_csv("./files/film_names.csv")

# file = open("./files/actors_more_than_2.csv", "r")

for i, j in df_actorsMoreThanTwo.iterrows():
    actorList.append(j[1])

# for i in df_actorsMoreThanTwo.iteritems():
#     yList.append(i)

for i, j in df_filmsMoreThanTwo.iterrows():
    filmsList.append(j[1])

df = pd.read_csv("./files/film-actor-role.csv")

df.plot.scatter(x = actorList,y = filmsList)

# print(actorList)

# print(filmsList)