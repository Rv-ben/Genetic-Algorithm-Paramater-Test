from genetic import *
from board import *
import json

#Start node problem size at 4 end at 10 
#Start population at 2

ProbData = {}
PopData = {}

#Test for fixed ns values [5,6,7]
#Fixed probablity of no mutation to 1/10
count = 0
for ns in [5,6,7]:
    PopData[ns] = {2:0,4:0,6:0,8:0,10:0,12:0}
    for j in range(10):
        for p in range(2,14,2):
            objects = [board(ns) for i in range(p)]
            popTest = genetic(objects,ns,ns+1)
            popTest.preformGenetic()
            PopData[ns].update({p:PopData[ns][p] + popTest.getIterations()})
            print(str(count)+" out of 180 Probablity Fixed Test")
            count = count +1

print(str(count)+" out of 180 Probablity Fixed Test")

#Test for fixed ns values [5,6,7]
#Fixed population of 4
count = 0
for ns in [5,6,7]:
    ProbData[ns] = {1:0,2:0,3:0,4:0,5:0,6:0}
    for j in range(10):
        for p in range(6):
            objects = [board(ns) for i in range(4)]
            probTest = genetic(objects,ns,ns+p)
            probTest.preformGenetic()
            ProbData[ns].update({p+1:ProbData[ns][p+1] + probTest.getIterations()})
            print(str(count)+" out of 180 population Fixed Test")
            count = count +1

print(str(count)+" out of 180 PopulationFixed")

file1 = open('PopulationFixed.json','w')

file1.write(json.dumps(PopData))

file2 = open('PropablityFixed.json','w')

file2.write(json.dumps(ProbData))
