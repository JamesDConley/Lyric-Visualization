import pandas as pd
from langdetect import detect #We could actually use our trained word2vec TSNE embedding for this, since languages show up as distinct clusters! But this is easier
def deleteNonEnglish(text):
    #print(text)
    
    if type(text) != str or ''.join([letter for letter in text if letter.isalpha()]).strip() == "" or detect(text) != 'en':
        return ""
    return text
print(detect("War doesn't show who's right, just who's left."))
lyrics = pd.read_csv('lyrics.csv')
print(len(lyrics['lyrics']))
lyrics['lyrics'] = lyrics['lyrics'].apply(deleteNonEnglish)
lyrics = lyrics[lyrics.lyrics!= ""]
print(len(lyrics['lyrics']))
lyrics.to_csv('cleanedLyrics.csv')
