import sys, os
import re

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

with open(filename) as f:
    for line in f:




class Player:

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
    






