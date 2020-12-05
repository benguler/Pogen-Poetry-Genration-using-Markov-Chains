from MarkovAgent import MarkovAgent
from markov import MarkovMatrix
from PoemUtility import PoemUtility
import syllables

class Poem:
    def __init__(self, markov, initWord, numLines, numSyl, category):
        self.markov = markov
        self.initWord = initWord
        self.numLines = numLines
        self.numSyl = numSyl
        self.category = category
        
    def generatePoem(self, iterations):
        agent = MarkovAgent(self.markov, self.initWord)
        poem = ""
        
        for i in range(self.numLines):   
            bestLine = ""
            
            for j in range(iterations):
                tmpLine = ""
                
                seed = agent.getWord()
                sylCount = 0
                
                while(sylCount != self.numSyl[i]):
                    tmpLine += agent.getWord()[len(agent.getWord()) - 1] + " "
                    sylCount += syllables.estimate(agent.getWord()[len(agent.getWord()) - 1])
                    
                    agent.transition()
                    
                    if(sylCount > self.numSyl[i]):
                        tmpLine = ""
                        sylCount = 0
                        agent.setWord(seed)
                        break
                    
                if(self.nbDist(tmpLine) >= self.nbDist(bestLine)):
                    bestLine = tmpLine
                    
            poem += bestLine
            poem += "\n"
            
        return poem
        
    def nbDist(self, line):
        #Get NaiveBayes probability distribution for category 
        return PoemUtility.classifySentence(line, self.category)
        
        return 0
    
