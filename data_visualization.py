import numpy as np
import pandas as pd
import csv

actorList = []

df_moreThanTwo = pd.read_csv("./files/actors_more_than_2.csv")

# for i, j in df_moreThanTwo.iterrows():
#     print(j)

for i in df_moreThanTwo.iterrows():
    print(i)

df = pd.read_csv("./files/film-actor-role.csv")

# df.plot.scatter(x = ,y)