 import MarkovAgent
 
 class Poem:
    def _init_(matrix, words, initWord, numLines, numWords, catagory):
        self.matrix = matrix
        self.words = words
        self.initWord = initWord
        self.numLines = numLines
        self.numWords = numWords
        self.catagory = catagory
        
    def generatePoem(iterations):
        agent = MarkovAgent(self.matrix, self.words, self.initWord)
        poem = ""
        
        for i in range(self.numLines):
            
            bestLine = ""
            
            for j in range(iterations):
                tmpLine = ""
                
                for k in range(self.numWords):
                    tmpLine += agent.getWord() + " "
                    
                    agent.transition()
                    
                if(nbDist(line) > nbDist(bestLine)):
                    bestLine = line
                    
            poem += bestLine
            poem += "\n"
            
        return poem
        
    def nbDist(line):
        #Get NaiveBayes probability distance for catagory 
        return 0
        