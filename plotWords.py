import matplotlib.pyplot as plt
import pickle
import pandas as pd
import time
import plotly as plotly
py = plotly.offline
import plotly.graph_objs as go
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

w2v = pickleLoad('w2v.pickle')
embedded = pickleLoad('embedded.pickle')
#plt.figure()
points = pd.DataFrame(
    [
        (word, coords[0], coords[1])
        for word, coords in [
            (word, embedded[w2v.wv.vocab[word].index])
            for word in w2v.wv.vocab if word!= ''
        ]
    ],
    columns=["word", "x", "y"]
)
  

N = 100000

trace = go.Scattergl(
    x = points['x'], 
    y = points['y'],
    text = points['word'], 
    mode = 'markers',
    marker = dict(
        color = '#FFBAD2',
        line = dict(width = 1)
    )
)
print("this far")
data = [trace]
layout = plotly.graph_objs.Layout(hovermode='closest')
figure = plotly.graph_objs.Figure(data=data, layout=layout)
print("that far")
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

