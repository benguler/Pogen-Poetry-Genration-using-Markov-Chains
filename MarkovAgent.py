import random

class MarkovAgent:
    def _init_(matrix, words, word):
        self.matrix = matrix
        self.words = words
        self.word
        
    def transition():
        index = self.words.index(self.word)
        
        prevProbs = 0.0
        
        for i in range (len(self.words)):
            rand01 = random.uniform(0, 1)
            
            if(matrix[index][j]) > rand01 or (matrix[index][i] + prevProb) >= 0.99999:
                self.word = self.words[i]
            
            prevProb += matrix[index][i]
        
    def getWord():
        return self.word