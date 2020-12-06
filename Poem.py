from MarkovAgent import MarkovAgent
from markov import MarkovMatrix
from PoemUtility import PoemUtility
import syllables

class Poem:
    def __init__(self, markov, initState, numLines, numSyl, category):
        #params: markov matrix, initial state, number of lines, number of syllables per line, category of poem
        self.markov = markov
        self.initState = initState
        self.numLines = numLines
        self.numSyl = numSyl
        self.category = category
        
    def generatePoem(self, iterations):
        #param: Number of iteration to run Naive-Bayes classification
        #Generate poem given specifications in constructor
        agent = MarkovAgent(self.markov, self.initState)
        poem = ""
        
        #For each line of the poem
        for i in range(self.numLines):   
            bestLine = ""
            
            #Generate line for poem and run nb classification for num of iterations
            for j in range(iterations):
                tmpLine = ""
                seed = agent.getState()
                
                sylCount = 0
                
                for i in range(len(agent.getState()) - 1):
                    tmpLine += agent.getState()[i] + " "
                    sylCount += syllables.estimate(agent.getState()[i])
                
                sylCount = syllables.estimate(tmpLine)
                
                #Generate line with roughly correct number of syllables
                while(sylCount < self.numSyl[i]):
                    tmpLine += agent.getState()[len(agent.getState()) - 1] + " "
                    sylCount += syllables.estimate(agent.getState()[len(agent.getState()) - 1])
                    agent.transition()
                    
                    """
                    if(sylCount > self.numSyl[i]):
                        print(tmpLine)
                        tmpLine = ""
                        agent.setState(seed)
                        
                        sylCount = 0
                        
                        for i in range(len(agent.getState()) - 1):
                            tmpLine += agent.getState()[i] + " "
                            
                        sylCount = syllables.estimate(tmpLine)
                    """
                    
                if(self.nbDist(tmpLine) >= self.nbDist(bestLine)):
                    bestLine = tmpLine
                    
            poem += bestLine
            poem += "\n"
            
            agent.transition()
            
        return poem
        
    def nbDist(self, line):
        #param: line to run Naive-Bayes classification on
        #Get NaiveBayes probability distribution for category 
        #return PoemUtility.classifySentence(line, self.category)
        
        return 0
    
