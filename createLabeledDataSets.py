import csv              #For reading from the CSV
import pickle           #For saving our Dictionaries so we don't have to run this whole thing each time!


#Reading in the raw data
lyricFile = open('lyrics.csv')      
csv_reader = csv.reader(lyricFile,  delimiter=',')

#Setting these here will make it easier to use this code on similar datasets
lyricColumn = 5
genreColumn = 4

genreListDict90 = {}
genreListDict10 = {}
count = 0
for row in csv_reader:
    #The first line just has the labels for each column so we skip it
    if count == 0:
        print("Skipped First Line")
        
    else:
        genreListDict = []
        if count % 10 == 0:
            genreListDict = genreListDict10
        else:
            genreListDict = genreListDict90
        
        
        if row[genreColumn] in genreListDict:
            lyrics = row[lyricColumn].replace(".", " ")
            lyrics = lyrics.replace("?", " ")
            lyrics = lyrics.replace("!",  " ")
            lyrics = lyrics.replace("\n",  " ")
            lyrics = lyrics.lower()
            
            lyrics = ''.join(item for item in lyrics if (item.isalpha() or item == ' '))
            #print(lyrics)
            genreListDict[row[genreColumn]].append(lyrics)
        else:
            genreListDict[row[genreColumn]] = []
    count+=1

pickleOut = open('genreListDict90.pickle', 'wb')
pickle.dump(genreListDict90, pickleOut)
pickleOut.close()

pickleOut = open("genreListDict10.pickle", "wb")
pickle.dump(genreListDict10, pickleOut)
pickleOut.close()

print("done")
