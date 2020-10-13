from genetic import *
from board import *
import json

#Start node problem size at 4 end at 10 
#Start population at 2

fixedPropData = {}
fixedPopData = {}

#Test for fixed ns values [5,6,7]
#Fixed probablity of no mutation to 1/10
count = 0
for ns in [5,6,7]:
    fixedPropData.update({ns:[]})
    for j in range(10):
        for p in range(2,12,2):
            objects = [board(ns) for i in range(p)]
            popTest = genetic(objects,ns,ns+1)
            popTest.preformGenetic()
            fixedPropData[ns].append((p,popTest.getIterations()))
            print(str(count)+" out of 150 Probablity Fixed Test")
            count = count +1

print(str(count)+" out of 150 Probablity Fixed Test")

#Test for fixed ns values [5,6,7]
#Fixed population of 4
count = 0
for ns in [5,6,7]:
    fixedPopData.update({ns:[]})
    for j in range(10):
        for p in range(5):
            objects = [board(ns) for i in range(4)]
            probTest = genetic(objects,ns,ns+p)
            probTest.preformGenetic()
            fixedPopData[ns].append((p,probTest.getIterations()))
            print(str(count)+" out of 150 population Fixed Test")
            count = count +1

print(str(count)+" out of 150 PopulationFixed")

file1 = open('PopulationFixed.json','w')

json.dump(fixedPopData,file1)


file2 = open('PropablityFixed.json','w')

json.dump(fixedPropData,file1)