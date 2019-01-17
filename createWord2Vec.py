import csv
from gensim.models import Word2Vec
import pickle
import multiprocessing
import time

startTime = time.clock()

def pickleSave(filename,  object):
    pickleOut = open('pickledObjects/' + filename,  'wb')
    pickle.dump(object,  pickleOut)
    pickleOut.close()

def pickleLoad(filename):
    pickleIn = open('pickledObjects/' + filename,  'rb')
    temp = pickle.load(pickleIn)
    pickleIn.close()
    return temp
def removeNonAlpha(text):
    return ''.join(letter for letter in text if letter.isalpha() or letter == " ").lower()
genreDict = pickleLoad('genreDict.pickle')
def getCommonGenre(word):
    max = 0
    maxgenre = ''
    for genre in genreDict.keys():
        if word in genreDict[genre].keys() and genreDict[genre][word] > max:
            max = genreDict[genre][word]
            maxgenre = genre
    return maxgenre
#Reading in the raw data
lyricFile = open('cleanedLyrics.csv')      
csv_reader = csv.reader(lyricFile,  delimiter=',')

#Setting these here will make it easier to use this code on similar datasets
lyricColumn = 6
genreColumn = 5

lines = []

#Sentences will be lines of songs
for row in csv_reader:
    for line in row[lyricColumn].split("\n"):
        if row[genreColumn] not in ['Not Available',  'Other',  'Electronic']:
            words = removeNonAlpha(line).split(" ")
            lines.append(words)



w2v = Word2Vec(sg=1,  seed = 1,  size=100, window=7,sample = 1e-3,  min_count=25, workers=7)
w2v.build_vocab(lines)
#print(len(w2v.vocab))
w2v.train(lines,  total_examples = w2v.corpus_count,  epochs = 10)
pickleSave("w2v.pickle", w2v)
endTime = time.clock()
print(w2v.wv['love'])

print("Elapsed Minutes : " + str((endTime-startTime)/60))
