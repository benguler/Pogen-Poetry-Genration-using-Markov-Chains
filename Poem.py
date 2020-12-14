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
            score = 0
            
            #Generate line for poem and run nb classification until nb score is enough
            while(score < 0.7):
                line = ""
                
                sylCount = 0
                
                #Add initial state to poem (the seed), minus the last word of that state
                for i in range(agent.stateSize - 1):
                    line += agent.getState()[i] + " "
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #agent.stateSize - 1] == END) implies line is finished
                
                while(not(sylCount == syln and agent.getState()[agent.stateSize - 1] == END)):
                    if(sylCount > syln or agent.getLastWord() == END):    #If number of syllables has been surpassed or finished line has too few syllables 
                        #Restart with new line with new seed
                        agent.setState(self.genSeed())
                        
                        line = ""
                        
                        sylCount = 0
                        
                        for i in range(agent.stateSize - 1):
                            line += agent.getState()[i] + " "
                            sylCount += syllables.estimate(agent.getState()[i])
                    
                    line += agent.getLastWord() + " "    #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getLastWord()) #Update overall syllable count
                    
                    agent.transition()  #Have the agent transition to a new state for next round of testing/next line
                    
                score = self.nbDist(line)

            poem += line
            poem += "\n"
            
        return poem
    
    def genSeed(self):
        #Generate initial n words of the poem
        seed = tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
        
        if(len(seed) != self.markovMatrix.state_size): #If seed is wrong state size
            return self.genSeed()   #Retry
        
        return seed
        
    def nbDist(self, line):
        #param: line to run Naive-Bayes classification on
        #Get NaiveBayes probability distribution for category
        return PoemUtility.classifySentence(line, self.category)
        
        #Return 0 when not testing nb classification. Training takes too long
        return 0