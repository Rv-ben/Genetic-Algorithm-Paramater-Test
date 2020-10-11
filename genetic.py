import copy
import random

class genetic:

    objects = [] #List of self.objects to be used in genetic algorithm
    n = 0 #The length of the encoded string for an object
    selectionNum = 0
    solution = None
    iterations = 0 #Number of genetic iterations 

    def getSolution(self):
        return self.solution

    def getIterations(self):
        return self.iterations

    def __init__(self,objects,n):
        self.n = n
        self.objects = objects
        self.selectionNum = len(objects)

    def selection(self):
    
        #list of selections
        selections = []
        
        #sum of fitnesses
        fitSum = 0
        for x in self.objects:
            fitSum = fitSum + x.getFitness()
            
        #calculate and store all selections
        for x in self.objects:
            selections.append(x.getFitness()/fitSum)
        
        #List of indexies for surviving objects
        selectedIndexies = []
        
        #n selections
        for i in range(self.selectionNum):
            
            #Random Number 0-1
            r = random.uniform(0, 1)
            
            #Starting range for selection
            startRange  = 0
        
            #Ending range for selection
            endRange = selections[0]
            
            #n possible ranges
            for j in range(self.selectionNum-1):
                # StartRange <= r < EndRange 
                if(startRange <= r and r < endRange):
                    #Store index of the selected object
                    selectedIndexies.append(j)
                    break
                if(j==self.n-2):
                    selectedIndexies.append(j)
                
                #Update the range
                startRange = endRange
                endRange = endRange + selections[i]
        
        survivingObjects = []
        for i in selectedIndexies:
            survivingObjects.append(copy.copy(self.objects[i]))
        
        return survivingObjects

    def crossOver(self):
    
        for i in range(0,len(self.objects)-1,2): #Start at 0 iterate by 2 for pairs

            #Get a random index from 0 to (n-1) to split the encoded objects
            indexSplit = random.randint(1,self.n-1)
            
            #Get encodedself.objects from both self.objects
            object1Encode = self.objects[i].getEncodedArray()
            
            object2Encode = self.objects[i+1].getEncodedArray()
            
            #Set the encodedobject  = object1(firstHalf) + object2(secondHalf)
            self.objects[i].setEncodedArray( object1Encode[:indexSplit]+object2Encode[indexSplit:] ) 
            
            #Set the encodedobject  = object2(firstHalf) + object1(secondHalf)
            self.objects[i+1].setEncodedArray( object2Encode[:indexSplit]+object1Encode[indexSplit:] ) 

    def mutation(self):
    
        #Go through self.objects
        for object in self.objects:
            
            #Get random index to mutate 0-n
            mutatedIndex = random.randint(0,self.n)
            
            #Give a chance to not mutate
            if(mutatedIndex < self.n):
                
                #get encodedobject
                encodedobject = object.getEncodedArray()
                
                #mutate the index
                encodedobject[mutatedIndex] = random.randint(0,self.n-1)
                
                #update the object
                object.setEncodedArray(encodedobject)

    def preformGenetic(self):
        #list B is a list of objects
        
        #Sort the list by fitness
        self.objects = sorted(self.objects, key=lambda object:object.fitness)
        count = 0
        
        #While the object with best fitness is not equal to 0, the solution
        while(self.objects[0].getFitness() != 0):
            
            #increment count
            count = count + 1
            
            #Use the select function to get surviving objects
            self.objects = self.selection()

            #Preform CrossOver
            self.crossOver()

            #Preform Mutation
            self.mutation()
                
            #Sort objects by fitness
            self.objects = sorted(self.objects, key=lambda object:object.fitness)
        
        self.solution = self.objects[0]
        self.iterations = count