# compile all data and export as .csv

import pandas as pd
import numpy as np


# actors w/ 2 or more appearances
freqActors = \
    ['Maggie Cheung',
 'Leslie Cheung',
 'Brigitte Lin',
 'Gong Li',
 'Charlie Yeung',
 'Man-Lei Chan',
 'Ting Yip Ng',
 'Lee-Na Kwan',
 'Siu Ping-Lam',
 'Carina Lau',
 'Ziyi Zhang',
 'Faye Wong',
 'Rebecca Pan',
 'Andy Lau',
 'Tony Chiu-Wai Leung',
 'Takeshi Kaneshiro',
 'Shun Lau',
 'Jacky Cheung',
 'Chang Chen',
 'To-Hoi Kong']

# # actors w/ more than 2 appearances
freqActors1 = \
    ['Charlie Yeung',
 'Jacky Cheung',
 'Siu Ping-Lam',
 'Tony Chiu-Wai Leung',
 'Maggie Cheung',
 'Chang Chen',
 'Leslie Cheung',
 'To-Hoi Kong',
 'Carina Lau']


# actors w/ 2 or more appearances
filmsDict = \
    {'2046': ['Tony Chiu-Wai Leung',
          'Gong Li',
          'Faye Wong',
          'Ziyi Zhang',
          'Carina Lau',
          'Chang Chen',
          'Maggie Cheung',
          'Siu Ping-Lam',
          'To-Hoi Kong',
          'Ting Yip Ng'],
 'As Tears Go By': ['Andy Lau', 'Maggie Cheung', 'Jacky Cheung', 'To-Hoi Kong'],
 'Ashes of Time': ['Brigitte Lin',
                   'Leslie Cheung',
                   'Maggie Cheung',
                   'Tony Chiu-Wai Leung',
                   'Jacky Cheung',
                   'Carina Lau',
                   'Charlie Yeung',
                   'Shun Lau'],
 'Chungking Express': ['Brigitte Lin',
                       'Tony Chiu-Wai Leung',
                       'Faye Wong',
                       'Takeshi Kaneshiro',
                       'Lee-Na Kwan'],
 'Days of Being Wild': ['Leslie Cheung',
                        'Maggie Cheung',
                        'Andy Lau',
                        'Carina Lau',
                        'Rebecca Pan',
                        'Jacky Cheung',
                        'Tony Chiu-Wai Leung'],
 'Eros': ['Gong Li', 'Chang Chen'],
 'Fallen Angels': ['Takeshi Kaneshiro',
                   'Charlie Yeung',
                   'Man-Lei Chan',
                   'To-Hoi Kong',
                   'Lee-Na Kwan'],
 'Happy Together': ['Leslie Cheung', 'Tony Chiu-Wai Leung', 'Chang Chen'],
 'In the Mood for Love': ['Maggie Cheung',
                          'Tony Chiu-Wai Leung',
                          'Siu Ping-Lam',
                          'Rebecca Pan',
                          'Man-Lei Chan'],
 'The Grandmaster': ['Tony Chiu-Wai Leung',
                     'Shun Lau',
                     'Ting Yip Ng',
                     'Ziyi Zhang',
                     'Chang Chen',
                     'To-Hoi Kong',
                     'Siu Ping-Lam',
                     'Charlie Yeung']}

# actors w/ more than 2 appearances
filmsDict1 = \
    {'2046': ['Tony Chiu-Wai Leung',
          'Carina Lau',
          'Chang Chen',
          'Maggie Cheung',
          'Siu Ping-Lam',
          'To-Hoi Kong'],
 'As Tears Go By': ['Maggie Cheung', 'Jacky Cheung', 'To-Hoi Kong'],
 'Ashes of Time': ['Leslie Cheung',
                   'Maggie Cheung',
                   'Tony Chiu-Wai Leung',
                   'Jacky Cheung',
                   'Carina Lau',
                   'Charlie Yeung'],
 'Chungking Express': ['Tony Chiu-Wai Leung'],
 'Days of Being Wild': ['Leslie Cheung',
                        'Maggie Cheung',
                        'Carina Lau',
                        'Jacky Cheung',
                        'Tony Chiu-Wai Leung'],
 'Eros': ['Chang Chen'],
 'Fallen Angels': ['Charlie Yeung', 'To-Hoi Kong'],
 'Happy Together': ['Leslie Cheung', 'Tony Chiu-Wai Leung', 'Chang Chen'],
 'In the Mood for Love': ['Maggie Cheung',
                          'Tony Chiu-Wai Leung',
                          'Siu Ping-Lam'],
 'The Grandmaster': ['Tony Chiu-Wai Leung',
                     'Chang Chen',
                     'To-Hoi Kong',
                     'Siu Ping-Lam',
                     'Charlie Yeung']}

dictDf = pd.DataFrame.from_dict(filmsDict, orient = 'index')
dictDf1 = pd.DataFrame.from_dict(filmsDict1, orient = 'index')
# df = df.transpose
# actors w/ 2 or more appearances
dictDf.to_csv("film-actors_two_or_more.csv")
# actors w/ more than 2 appearances
dictDf1.to_csv("film-actors_more_than_2.csv")

listDf = pd.DataFrame(freqActors)
listDf1 = pd.DataFrame(freqActors1)

# actors w/ 2 or more appearances
listDf.to_csv("actors_two_or_more.csv")
# actors w/ 2 or more appearances
listDf1.to_csv("actors_more_than_2.csv")
