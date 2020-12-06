from MarkovAgent import MarkovAgent
from markov import MarkovMatrix
from PoemUtility import PoemUtility
import syllables

class Poem:
    def __init__(self, markovMatrix, numLines, numSyl, category):
        #params: markov probability matrix, number of lines, number of syllables per line, category of poem
        self.markovMatrix = markovMatrix
        self.numLines = numLines
        self.numSyl = numSyl
        self.category = category
        
    def generatePoem(self, iterations):
        
        #param: Number of iteration to run Naive-Bayes classification
        #Generate poem given specifications in constructor
        agent = MarkovAgent(self.markovMatrix, self.genSeed())
        poem = ""
        
        #For each line of the poem
        for i in range(self.numLines):  
            bestLine = ""
            
            #Generate line for poem and run nb classification for num of iterations
            for j in range(iterations):
                tmpLine = ""
                
                sylCount = 0
                
                #Add initial state to poem, minus the last word of that state
                for i in range(len(agent.getState()) - 1):
                    tmpLine += agent.getState()[i] + " "
                    sylCount += syllables.estimate(agent.getState()[i])
                
                #Generate line with roughly correct number of syllables
                #len(agent.getState()) - 1] == "___END__") implies line is finished
                while(not(sylCount == self.numSyl[i] and agent.getState()[len(agent.getState()) - 1] == "___END__")):
                    if(sylCount > self.numSyl[i] or agent.getState()[len(agent.getState()) - 1] == "___END__"):    #If number of syllables has been surpassed or finished line has too few syllables 
                        #Start new line with new seed
                        agent.setState(self.genSeed())
                        
                        tmpLine = ""
                        
                        sylCount = 0
                        
                        for i in range(len(agent.getState()) - 1):
                            tmpLine += agent.getState()[i] + " "
                            sylCount += syllables.estimate(agent.getState()[i])
                    
                    tmpLine += agent.getState()[len(agent.getState()) - 1] + " "    #Add the last word of the agent's current state to the line
                    sylCount += syllables.estimate(agent.getState()[len(agent.getState()) - 1]) #Record its syllable count
                    
                    agent.transition()  #Have the agent transition to a new state
                   
                if(self.nbDist(tmpLine) >= self.nbDist(bestLine)):  #If the current line scores better or equal to the best line
                    #best line = current line
                    bestLine = tmpLine
                    
                agent.setState(self.genSeed())  #Initialize seed for next iteration/line
                    
            poem += bestLine
            poem += "\n"
            
        return poem
        
    def nbDist(self, line):
        #param: line to run Naive-Bayes classification on
        #Get NaiveBayes probability distribution for category 
        #return PoemUtility.classifySentence(line, self.category)
        
        #Return 0 when not testing nb classification. Training takes too long
        return 0
        
    def genSeed(self):
        return tuple(self.markovMatrix.walk(None, self.markovMatrix.state_size))
    
