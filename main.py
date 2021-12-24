import csv
#import sys
#Background - https://cs50.harvard.edu/x/2020/psets/6/dna
#To find more tests look into cs50 ide . Pset6/dna/sequences 

header = [] #Database header. Stores the sequences to be compared -Array
database  = [] #Stores the profiles with their stats inline with the header. -2d Array

 #Stores a summary of the stats of the person to be compared.

#For example , ["Username", 10 , 17 , 200 ,223]. Each val after the name stores the highest streak of dna of a given dna strand
#Note to self: The database array stores the strands (in order) that are used for comparison.
'''
This string is necessary to be in userData.
The database has the persons name at idx 0. Therefore when we
iterate through userData and person(database record) to compare if its a match we
need them to be the same length.
'''

def main():
    #For command line arguements
    #load_dataBase(sys.argv[1])
    #userStats = load_userStats(sys.argv[2])
    load_dataBase("test.txt")
    userStats = load_userStats("userDNA.txt")
    
    maxIdx = 0
    hMatches = number_of_matches( userStats, database[0])

    for i in range(len(database)):
        curr = number_of_matches(userStats , database[i])
        if ( curr > hMatches ):
            maxIdx = i
            hMatches = curr

    print("User stats:", userStats)
    
    if (hMatches == 0):
        print("No match found")
    else:
        print("Most likely match: ", database[maxIdx] )
        print("Overlaps: ", hMatches)


#Input - takes in a list with the persons stats
def number_of_matches(userStats , personD):
    count = 0
  
    for j in range( 1 , len(personD) ):# start at 1 bc 0 holds the name which is something that doesnt need to be compared.
        if ( int(userStats[j]) == int(personD[j]) ):
            count += 1
            
    return count


def load_userStats(filename):
    userData = ["Username"]
    currFile = open(filename , "r")
    sHolder = " ".join([row for row in currFile])#dna is taken in as an array with one val
    #The sinle value is put as a string, easier to read

    #Need to map what the highest streak of each strand into an list
    for i in range(1, len(header) ):
        hold = findStreak( sHolder, header[i])
        userData.append(hold)
    return userData


def findStreak( dna  , pattern ):
    mSize = len(pattern)
    highest_Streak = 0
    currentStreak = 0
    idx = 0

    #Iterate and look for highest streak
    for tide in dna:
        if (tide == pattern[idx]):
            idx += 1
            if (idx >= mSize):
                idx = 0
                currentStreak += 1
                highest_Streak = max(currentStreak , highest_Streak)
        else:
            currentStreak = 0
            idx = 0
    return highest_Streak

def load_dataBase(filename):

    data = open(filename)
    reader = csv.reader(data)

    global header
    header = next(reader)

    global database
    database = [row for row in reader]
    
    
main()