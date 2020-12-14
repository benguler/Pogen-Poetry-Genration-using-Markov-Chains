from MarkovAgent import MarkovAgent
from markov import MarkovMatrix, ReverseMarkovMatrix
from PoemUtility import PoemUtility
import syllables
import pronouncing
import random

BEGIN = "___BEGIN__"
END = "___END__"

class Poem:
    def __init__(self, markovMatrix, numSyls, category):
        #params: markov probability matrix, number of syllables per line, category of poem (period_genre), bool that dictates if poem will have rhyming
        self.markovMatrix = markovMatrix
        self.numSyls = numSyls
        self.category = category

    def generatePoem(self):
        #Generate poem given specifications in constructor
        agent = MarkovAgent(self.markovMatrix, self.genSeed())  #Create agent with poem seed as initial state
        poem = ""
        
        #For each line of the poem
        for syln in self.numSyls:  
            line = ""
        
            score = 0
            
            #Generate line for poem and run nb classification until nb score is enough
            while(score < 0.2):
                line = ""
                
                sylCount = 0
                
                #Add initial state to poem (the seed), minus the last word of that state
                for i in range(agent.stateSize - 1):
                    line += agent.getState()[i] + " "
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #agent.stateSize - 1] == END) implies line is finished
                
                while(agent.getState()[agent.stateSize - 1] != END):                 
                    line += agent.getLastWord() + " "    #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getLastWord()) #Update overall syllable count
                    
                    agent.transition()  #Have the agent transition to a new state
                    
                score = self.nbDist(line)
                
                agent.setState(self.genSeed()) #Initialize agent state to new seed for next line/round of nb classification
            
            print("TEST 8")
            poem += line
            poem += "\n"
            
        print("TEST 3")
        return poem
    
    def genSeed(self):
        #Generate initial n words of the poem
        seed = tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
        
        print("TEST 4")
        
        if(len(seed) != self.markovMatrix.state_size): #If seed is wrong state size
            return self.genSeed()   #Retry
        
        return seed
        
    def nbDist(self, line):
        print("TEST 9")
        #param: line to run Naive-Bayes classification on
        #Get NaiveBayes probability distribution for category
        print(line, " ", PoemUtility.classifySentence(line, self.category))
        return PoemUtility.classifySentence(line, self.category)
        
        #Return 0 when not testing nb classification. Training takes too long
        return 0