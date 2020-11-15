 import MarkovAgent
 
 class Poem:
    def _init_(matrix, words, initWord, numLines, numWords):
        self.matrix = matrix
        self.words = words
        self.initWord = initWord
        self.numLines = numLines
        self.numWords = numWords
        
    def generatePoem():
        agent = MarkovAgent(self.matrix, self.words, self.initWord)
        poem = ""
        
        for i in range(self.numLines):
            for j in range(self.numWords):
                poem += agent.getWord() + " "
                
                agent.transition()
                
            poem += "\n"
            
        return poem
        