# format data from .csv for turning into pandas visualization

from data_filter import movob
import numpy as np
import pandas as pd
from imdb import IMDb
import pprint

ia = IMDb()

pp = pprint.PrettyPrinter(indent=1)

Gt2 = open("../files/film-actors_more_than_2.csv", "r")

Gt2orE = open("../files/film-actors_two_or_more.csv", "r")

for i in Gt2:
    print(i)