import copy
import random

class genetic:

    def selection(self,objects,n):
    
        #list of selections
        selections = []
        
        #sum of fitnesses
        fitSum = 0
        for x in objects:
            fitSum = fitSum + x.getFitness()
            
        #calculate and store all selections
        for x in objects:
            selections.append(x.getFitness()/fitSum)
        
        #List of indexies for surviving objects
        selectedIndexies = []
        
        #n selections
        for i in range(n):
            
            #Random Number 0-1
            r = random.uniform(0, 1)
            
            #Starting range for selection
            startRange  = 0
        
            #Ending range for selection
            endRange = selections[0]
            
            #n possible ranges
            for j in range(n-1):
                # StartRange <= r < EndRange 
                if(startRange <= r and r < endRange):
                    #Store index of the selected board
                    selectedIndexies.append(j)
                    break
                if(j==n-2):
                    selectedIndexies.append(j)
                
                #Update the range
                startRange = endRange
                endRange = endRange + selections[i]
        
        survivingobjects = []
        for i in selectedIndexies:
            survivingobjects.append(copy.copy(objects[i]))
        
        return survivingobjects

    def crossOver(self,objects,n):
    
        for i in range(0,len(objects)-1,2): #Start at 0 iterate by 2 for pairs

            #Get a random index from 0 to (n-1) to split the encoded objects
            indexSplit = random.randint(1,n-1)
            
            #Get encodedobjects from both objects
            board1Encode = objects[i].getEncodedArray()
            
            board2Encode = objects[i+1].getEncodedArray()
            
            #Set the encodedBoard  = board1(firstHalf) + board2(secondHalf)
            objects[i].setEncodedArray( board1Encode[:indexSplit]+board2Encode[indexSplit:] ) 
            
            #Set the encodedBoard  = board2(firstHalf) + board1(secondHalf)
            objects[i+1].setEncodedArray( board2Encode[:indexSplit]+board1Encode[indexSplit:] ) 

    def mutation(self,objects,n):
    
        #Go through objects
        for board in objects:
            
            #Get random index to mutate 0-n
            mutatedIndex = random.randint(0,n)
            
            #Give a chance to not mutate
            if(mutatedIndex < n):
                
                #get encodedBoard
                encodedBoard = board.getEncodedArray()
                
                #mutate the index
                encodedBoard[mutatedIndex] = random.randint(0,n-1)
                
                #update the board
                board.setEncodedArray(encodedBoard)