import csv              #For reading from the CSV
import pickle           #For saving our Dictionaries so we don't have to run this whole thing each time!


#Reading in the raw data
lyricFile = open('cleanedLyrics.csv')      
csv_reader = csv.reader(lyricFile,  delimiter=',')
def pickleSave(filename,  object):
    pickleOut = open('pickledObjects/' + filename,  'wb')
    pickle.dump(object,  pickleOut)
    pickleOut.close()

def pickleLoad(filename):
    pickleIn = open('pickledObjects/' + filename,  'rb')
    temp = pickle.load(pickleIn)
    pickleIn.close()
    return temp

#Setting these here will make it easier to use this code on similar datasets
lyricColumn = 6
genreColumn = 5

#This dictionary will be indexed with a genre to produce another dictionary that takes in a word and gives the frequency of that word within that genre
genres = {}

#Keeps track of the row we are currently in while looping
count = 0

#This dictionary keeps track of the count for all words irrespective of genre, index it with a word and it will give the frequency throughout all genres
globalFrequencyDict = {}
globalFrequencyDict["total words"] = 0 #Add an entry for the total number of words globally, we know this is a safe index because all others will have no whitespace
for row in csv_reader:
    #The first line just has the labels for each column so we skip it
    if count == 0:
        print("Skipped First Line")
        count+=1
        
    else:
        if row[genreColumn] not in ['Not Available',  'Other',  'Electronic']:
            genreDict = {}  #Dummy Variable
            if row[genreColumn] in genres:
                genreDict = genres[row[genreColumn]]    #If we already have a dictionary for this genre do nothing (we don't use this variable)
            else:
                genres[row[genreColumn]] = {}               #If we don't have a dictionary for this genre, add one
                genres[row[genreColumn]]["total words"] = 0 #Add an entry to keep track of the total number of words in this genre (We know "total words" is a safe entry because all other indexes will have no whitespace
            #This section does a similar stint within the given genre for each word
            lyrics = row[lyricColumn].replace(".", " ")
            lyrics = lyrics.replace("?", " ")
            lyrics = lyrics.replace("!",  " ")
            lyrics = lyrics.replace("\n",  " ")
            for word in lyrics.split(' '):
                #Convert all words to lowercase, removing everything but letters
                cleanedWord = word.lower()
                cleanedWord = ''.join(letter for letter in cleanedWord if letter.isalpha() )
                
                #Now fill up the dictionary!
                if cleanedWord in genres[row[genreColumn]]:
                    genres[row[genreColumn]][cleanedWord] +=1
                else:
                    genres[row[genreColumn]][cleanedWord] = 1
                genres[row[genreColumn]]["total words"]+=1
                
                if cleanedWord in globalFrequencyDict:
                    globalFrequencyDict[cleanedWord] +=1
                else:
                   globalFrequencyDict[cleanedWord] = 1
                globalFrequencyDict["total words"]+=1
        count+=1
#Write out the genre dictionaries!
pickleSave( "genreDict.pickle", genres)

#Write out the global dictionary!
pickleSave(  "wordFrequencyDict.pickle", globalFrequencyDict)

print("done")
