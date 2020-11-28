import MarkovAgent
from markov import MarkovMatrix
 
class Poem:
    def _init_(self, markov, words, initWord, numLines, numWords, category):
        self.markov = markov
        self.initWord = initWord
        self.numLines = numLines
        self.numWords = numWords
        self.category = category

    def nbDist(self, line):
        #Get NaiveBayes probability distance for category
        return 0
        
    def generatePoem(self, iterations):
        agent = MarkovAgent(self.markov, self.initWord)
        poem = ""
        
        for i in range(self.numLines):   
            bestLine = ""
            
            for j in range(self.iterations):
                tmpLine = ""
                
                for k in range(self.numWords):
                    tmpLine += agent.getWord() + " "
                    
                    agent.transition()
                    
                if(self.nbDist(tmpLine) > self.nbDist(bestLine)):
                    bestLine = tmpLine
                    
            poem += bestLine
            poem += "\n"
            
        return poem