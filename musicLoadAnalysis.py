import pickle
import heapq
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
def pickleSave(filename,  object):
    pickleOut = open('pickledObjects/' + filename,  'wb')
    pickle.dump(object,  pickleOut)
    pickleOut.close()

def pickleLoad(filename):
    pickleIn = open('pickledObjects/' + filename,  'rb')
    temp = pickle.load(pickleIn)
    pickleIn.close()
    return temp
genreHeapsDict = {}
genresDict = pickleLoad("genreDict.pickle")

globalDict = pickleLoad("wordFrequencyDict.pickle")



print(genresDict.keys())
for genre in genresDict.keys():
    genreHeapsDict[genre] = []
    for word in genresDict[genre].keys():
        if not word in stopwords.words('english'):
            heapq.heappush( genreHeapsDict[genre],  (0 - (((genresDict[genre][word])/genresDict[genre]["total words"])-(globalDict[word]/globalDict["total words"])),  word) )

for key in genreHeapsDict.keys():
    print(key)
    heap = genreHeapsDict[key]
    for i in range(50):
        print(heapq.heappop(heap))
    



    

