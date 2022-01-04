from data import updatedDict, filmsList
import pprint

pp = pprint.PrettyPrinter()

knownActors = []

for i in filmsList:
    # knownActors.append(updatedDict[i])
    for k in range(len(updatedDict[i])):
        # print(k)
        knownActors.append(updatedDict[i][k])
# print(knownActors)

knownActors = list(set(knownActors))

pp.pprint(knownActors)