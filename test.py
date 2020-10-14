from genetic import *
from board import *
import json
import threading
import logging

#Start node problem size at 4 end at 10 
#Start population at 2



def computeProbFixed(trials):
    PopData = {}
    #Test for fixed ns values [5,6,7]
    #Fixed probablity of no mutation to 1/10
    count1 = 0
    for ns in [4,5,6,7]:
        PopData[ns] = {2:0,4:0,6:0,8:0,10:0,12:0,14:0}
        for j in range(trials):
            for p in range(2,16,2):
                objects = [board(ns) for i in range(p)]
                popTest = genetic(objects,ns,ns+1)
                popTest.preformGenetic()
                PopData[ns].update({p:PopData[ns][p] + popTest.getIterations()})
                logging.info(str(count1)+" out of 180 Probablity Fixed Test")
                count1 = count1 +1
    

    logging.info(str(count1)+" out of 180 Probablity Fixed Test")

    file1 = open('ProbablityFixed.json','w')

    file1.write(json.dumps(PopData))

def computePopFixed(trials):
    #Test for fixed ns values [5,6,7]
    #Fixed population of 4
    ProbData = {}
    count2 = 0
    for ns in [4,5,6,7]:
        ProbData[ns] = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}
        for j in range(trials):
            for p in range(7):
                objects = [board(ns) for i in range(8)]
                probTest = genetic(objects,ns,ns+p)
                probTest.preformGenetic()
                ProbData[ns].update({p+1:ProbData[ns][p+1] + probTest.getIterations()})
                logging.info(str(count2)+" out of 180 population Fixed Test")
                count2 = count2 +1

    logging.info(str(count2)+" out of 180 PopulationFixed")

    file2 = open('PopulationFixed.json','w')

    file2.write(json.dumps(ProbData))

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")

popFixed = threading.Thread(target=computePopFixed,args=(100))
probFixed = threading.Thread(target=computeProbFixed,args=(100))

popFixed.start()
probFixed.start()

popFixed.join()
probFixed.join()
