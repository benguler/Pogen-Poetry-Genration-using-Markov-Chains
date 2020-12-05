from MarkovAgent import MarkovAgent
from markov import MarkovMatrix
from PoemUtility import PoemUtility
import syllables

class Poem:
    def _init_(markov, words, initWord, numLines, numSyl, category):
        self.markov = markov
        self.initWord = initWord
        self.numLines = numLines
        self.numWords = numWords
        self.category = category
        
    def generatePoem(iterations):
        agent = MarkovAgent(self.markov, self.initWord)
        poem = ""
        
        for i in range(self.numLines):   
            bestLine = ""
            
            for j in range(self.iterations):
                tmpLine = ""
                
                seed = agent.getWord()
                sylCount = 0
                
                while(sylCount != numSyl[i]):
                    tmpLine += agent.getWord() + " "
                    sylCount += syllables.estiamte(agent.getWord())
                    
                    agent.transition()
                    
                    if(sylCount > numSyl[i]):
                        tmpLine = ""
                        sylCount = 0
                        agent.setWord(seed)
                    
                if(nbDist(line) > nbDist(bestLine)):
                    bestLine = line
                    
            poem += bestLine
            poem += "\n"
            
        return poem
        
    def nbDist(line):
        #Get NaiveBayes probability distance for category 
        return PoemUtility.classifySentence(line)
    