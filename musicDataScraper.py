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
    #First fine all the song titles on the page
    soup = BeautifulSoup(page.content, 'html.parser')  
    titles = soup.findAll("span", {'class':'chart-list-item__title-text'})
    for i in range(len(titles)):
        titles[i] = titles[i].text.replace('\n','')
    
    #Then find all the artists for these songs
    artists = soup.findAll("div", {'class':'chart-list-item__artist'})
    for i in range(len(artists)):
        artists[i] = artists[i].text.replace('\n', '') 
    
    #It's useful to combine the artists and song titles in order to find the right lyrics
    fullTitles = []
    for i in range(len(titles)):
        fullTitles.append((artists[i] + "-" + titles[i]).replace(' ', '-'))
    
    #Now get the lyrics for each song through genius.com
    lyricBaseAddress = "https://genius.com/"
    lyrics = []
    for title in fullTitles:
        address = lyricBaseAddress + title + "-lyrics"
        newSoup = BeautifulSoup(requests.get(address).content, 'html.parser')
        lyrics.append(newSoup.find('p').text)
        time.sleep(.1)  #We could be making a large number of requests to the same site so we are ratelimiting our requests
    return artists, titles, lyrics

#Main Script
genres = genresDict.keys()
pages = []
genresListsDict = {}
for genre in genres:
    genresListsDict[genre]=pageToLists(requests.get(baseAddress+genresDict[genre]))
    artists,  titles,  lyrics = genresListsDict[genre]
    #Write the data to a text file
    dataFile = open(genre+'-lyricData.txt', 'w+')
    for i in range(len(artists)):
        dataFile.write(str(artists[i])+'\n'+str(titles[i])+'\n'+str(lyrics[i]))
    
    
