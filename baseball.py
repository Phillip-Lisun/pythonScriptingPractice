import sys, os
import re
from collections import OrderedDict

class Player: #player class, holds name, total bats, total hits

    def __init__(self, name):
        self.name = name
        self.hits = 0
        self.bat = 0

    def addHits(self, hits):
        self.hits = self.hits + hits

    def totalBat(self, bats):
        self.bat = self.bat + bats

    def average(self):
        average = self.hits / self.bat
        return average
    
    def getName(self):
        return self.name

if len(sys.argv) < 2: #usage function
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")
    
lineRegex = re.compile(r"(^\S+\s\S+\s)(\S+\s)(\d+\s)(\S+\s){2}(\d+\s)(\S+\s){2}(\d+\s)(\S+)") #regex for line
playerName = [] #list to hold player names (to see if we've already made the object)
playerObject = [] #list to hold all the player objects

with open(filename) as f: 
    for line in f: #checks each line
        line = line.strip() #selects the line
        if lineRegex.match(line): #checks to see if it matches the regex 
            match = lineRegex.match(line)
            name = (match.group(1)) 
            
            
            if name not in playerName: 
                playerName.append(name)
                
                thisPlayer = Player(name)
                batted = int(match.group(3)) #gets bats to add
                hits = int(match.group(5))  #gets hits to add
                
                thisPlayer.addHits(hits) #adds hits to object
                thisPlayer.totalBat(batted) #adds bats to object
                
                playerObject.append(thisPlayer) #adds object to list
                
            else:
                
                batted = int(match.group(3))
                hits = int(match.group(5))
                
                for player in playerObject: #finds the object, adds bats and hits
                    checkName = player.getName()
                    if checkName == name:
                        player.addHits(hits)
                        player.totalBat(batted)

outputStats = {} 

for Player in playerObject: #gets the average, and puts in a dictionary
    average = Player.average()
    average = round(average, 3)
    name = Player.getName()
    average = (f"{average:.3f}") #formats to include trailing 0s
    
    outputStats[name] = average


outputStats = OrderedDict(sorted(outputStats.items(), key=lambda x:x[1], reverse=True)) #sorts the dictionary by values


for name in outputStats: #prints results
    print(name,':',outputStats[name])