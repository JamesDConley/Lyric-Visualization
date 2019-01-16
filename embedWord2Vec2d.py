import pickle
import pandas as pd
from MulticoreTSNE import MulticoreTSNE as TSNE
import numpy as np
import time
import heapq
def removeNonAlpha(text):
    return ''.join(letter for letter in text if letter.isalpha() or letter == " ").lower()
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
startTime = time.clock()
w2v = pickleLoad('w2v.pickle')
#all_word_vectors_matrix = w2v.wv.syn0
wordFrequencyDict = pickleLoad('wordFrequencyDict.pickle')
wordFrequencyDict['total words']=0

frequentWordsHeap = []
print(1)
for key in wordFrequencyDict.keys():
    heapq.heappush(frequentWordsHeap,  (-wordFrequencyDict[key],  removeNonAlpha(key)))
print(2)
top10kWords = []
top10kVectors = []

for i in range(10000):
    
    top10kWords.append(heapq.heappop(frequentWordsHeap)[1])
    
    top10kVectors.append(w2v.wv[top10kWords[i]])
top10kWords = np.array(top10kWords)
top10kVectors = np.array(top10kVectors)

print("loaded")


embedded = TSNE(n_jobs=7).fit_transform(top10kVectors)
print("done")

points = pd.DataFrame(
    [
        (word, coords[0], coords[1])
        for word, coords in [
            (top10kWords[i], embedded[i])
            for i in range(len(top10kWords))
        ]
    ],
    columns=["word", "x", "y"]
)

pickleSave('points.pickle',  points)
pickleSave('embedded.pickle',  embedded)
endTime = time.clock()
print("Elapsed Minutes : " + str((endTime-startTime)/60))
