import pickle
import pandas as pd
import plotly as plotly
import math
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
    maxgenre = 'Indie'
    for genre in genreDict.keys():
        if word in genreDict[genre].keys() and genreDict[genre][word] > max:
            max = genreDict[genre][word]
            maxgenre = genre
    return maxgenre
w2v = pickleLoad('w2v.pickle')
embedded = pickleLoad('embedded.pickle')
points = pickleLoad('points.pickle')
frequencyDict = pickleLoad('wordFrequencyDict.pickle')
sizes = []
for word in points['word']:
    sizes.append(math.log(frequencyDict[word], 1.8))
points['size'] = pd.Series(sizes)

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
genres = [e for e in genreDict.keys()]
colors = ['#800000','#ffe119','#3cc44b',"#000075",'#911eb4',"#e6194b","#808000","#000000","#ffd8b1"]
for i in range(len(genreDict.keys())):
    tempColor = colors[i]
    genre = genres[i]
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
                color = tempColor,
                line = dict(width = 1), 
                size = tempPoints['size']
            ), name = genre
    ))



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

