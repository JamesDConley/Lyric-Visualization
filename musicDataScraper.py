import requests
from bs4 import BeautifulSoup
import time
baseAddress = "https://www.billboard.com/charts/"
genresDict = {
    "pop":"adult-pop-songs/", 
    "country":"country-songs", 
    "rock":"rock-songs", 
    "rap":"rap-song"
    }
def pageToLists(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.findAll("span", {'class':'chart-list-item__title-text'})
    for i in range(len(titles)):
        titles[i] = titles[i].text.replace('\n','')
    
    artists = soup.findAll("div", {'class':'chart-list-item__artist'})
    for i in range(len(artists)):
        artists[i] = artists[i].text.replace('\n', '') 
    
    
    print(len(titles))
    fullTitles = []
    for i in range(len(titles)):
        fullTitles.append((artists[i] + "-" + titles[i]).replace(' ', '-'))
    #lyricLinksNewList = [item for sublist in lyricLinks for item in sublist]
    
    #print(fullTitles)
    
    
    #Now get the lyrics for each song
    lyricBaseAddress = "https://genius.com/"
    lyrics = []
    for title in fullTitles:
        address = lyricBaseAddress + title + "-lyrics"
        newSoup = BeautifulSoup(requests.get(address).content, 'html.parser')
        lyrics.append(newSoup.find('p').text)
        time.sleep(.1)
        print(address)
        print(lyrics)
    
    
    return artists, titles, lyrics
genres = genresDict.keys()
pages = []
genresListsDict = {}
for genre in genres:
    genresListsDict[genre]=pageToLists(requests.get(baseAddress+genresDict[genre]))
    artists,  titles,  lyrics = genresListsDict[genre]
    dataFile = open(genre+'-lyricData.txt', 'w+')
    for i in range(len(artists)):
        dataFile.write(str(artists[i])+'\n'+str(titles[i])+'\n'+str(lyrics[i]))
    
#for genre in genres:
 #   pages.append(requests.get(baseAddress + genresDict[genre]))
    
