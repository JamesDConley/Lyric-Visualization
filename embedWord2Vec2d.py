import pickle
import sklearn.manifold
import pandas as pd
import seaborn as sns
#from tsnecuda import TSNE
from MulticoreTSNE import MulticoreTSNE as TSNE
from gensim.models import Word2Vec
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
startTime = time.clock()
w2v = pickleLoad('w2v.pickle')
#all_word_vectors_matrix = w2v.wv.syn0
print("loaded")
embedded = TSNE(n_jobs=7).fit_transform(w2v.wv.syn0)


all_word_vectors_matrix_2d = embedded
print("done")
points = pd.DataFrame(
    [
        (word, coords[0], coords[1])
        for word, coords in [
            (word, all_word_vectors_matrix_2d[w2v.wv.vocab[word].index])
            for word in w2v.wv.vocab
        ]
    ],
    columns=["word", "x", "y"]
)
pickleSave('embedded.pickle',  embedded)
endTime = time.clock()
print("Elapsed Minutes : " + str((endTime-startTime)/60))
#sns.set_context("poster")
#points.plot.scatter("x", "y", s=10, figsize=(20, 12))
