import matplotlib.pyplot as plt
import pickle
import pandas as pd
import time
import plotly as plotly
py = plotly.offline
import random
import numpy as np
def pickleLoad(filename):
    pickleIn = open(filename,  'rb')
    temp = pickle.load(pickleIn)
    pickleIn.close()
    return temp
def pickleSave(filename,  object):
    pickleOut = open(filename,  'wb')
    pickle.dump(object,  pickleOut)
    pickleOut.close()
genreDict = pickleLoad('genreDict.pickle')
def getCommonGenre(word):
    max = 0
    maxgenre = ''
    for genre in genreDict.keys():
        if word in genreDict[genre].keys() and genreDict[genre][word] > max:
            max = genreDict[genre][word]
            maxgenre = genre
    return maxgenre
w2v = pickleLoad('w2v.pickle')
embedded = pickleLoad('embedded.pickle')
#plt.figure()
points = pickleLoad('points.pickle')


import plotly as plotly
py = plotly.offline
import plotly.graph_objs as go
genreLists = {}
for genre in genreDict.keys():
    genreLists[genre] = []
for word in points['word']:
    #print(word)
    genre = getCommonGenre(word)
    genreLists[genre].append(word)
scatters = []
print(0)
for genre in genreDict.keys():
    tempPoints = points.loc[points['word'].isin(genreLists[genre])]
    randColor = ("#%06x" % random.randint(0, 0xFFFFFF))
    print(1)
    scatters.append(
        go.Scattergl(
            x = tempPoints['x'], 
            y = tempPoints['y'],
            text = tempPoints['word'], 
            mode = 'markers',
            marker = dict(
                color = randColor,
                line = dict(width = 1)
            ), name = genre
    ))

trace = go.Scattergl(
    x = points['x'], 
    y = points['y'],
    text = points['word'], 
    mode = 'markers',
    marker = dict(
        color = "#FFBAD2",
        line = dict(width = 1)
    )
)

#data = [trace]
data = scatters
layout = plotly.graph_objs.Layout(hovermode='closest')
figure = plotly.graph_objs.Figure(data=data, layout=layout)
py.plot(figure)
  
#points.plot.scatter("x", "y", s=1)
#print(points)
#plt.show()

#for index, row in points.iterrows():
#    plt.annotate(row[0],  (row[1], row[2]))
#    if index+1 %100 == 0:
#        break


#plt.show()
print("plotted")
#time.sleep(10)

