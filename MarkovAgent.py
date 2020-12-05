import random
from markov import MarkovMatrix

class MarkovAgent:
    def __init__(self, markov, initWord):
        self.markov = markov
        self.word = initWord
        
        self.markov = markov
    
    def transition(self):
        self.word = ((self.markov.move(self.word), ))
        
    def getWord(self):
        return self.word
        
    def setWord(self, word):
        self.word = word
        
    