import pickle
import heapq
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
genreHeapsDict = {}
pickleIn = open("genreDict.pickle",  "rb")
genresDict = pickle.load(pickleIn)
pickleIn.close()

pickleIn = open("wordFrequencyDict.pickle",  "rb")
globalDict = pickle.load(pickleIn)
pickleIn.close()



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
    



    

