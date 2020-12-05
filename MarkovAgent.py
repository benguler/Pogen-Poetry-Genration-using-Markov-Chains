import random
from markov import MarkovMatrix

class MarkovAgent:
    def _init_(markov, initWord):
        self.markov = markov
        self.word = initWord
        
        self.markov = markov
    
    def transition():
        self.word = self.markov.move(self.word)
        
    def getWord():
        return self.word
        
    def setWord(word):
        self.word = word
        
    