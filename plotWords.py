import matplotlib.pyplot as plt
import pickle
import pandas as pd
import time
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
  
points.plot.scatter("x", "y", s=1)
#print(points)
#plt.show()

#for index, row in points.iterrows():
#    plt.annotate(row[0],  (row[1], row[2]))
#    if index+1 %100 == 0:
#        break


plt.show()
print("plotted")
#time.sleep(10)

