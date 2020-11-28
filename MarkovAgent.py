import random
from markov import MarkovMatrix

class MarkovAgent:
    def _init_(self, markov, initWord):
        self.markov = markov
        self.word = initWord

    def transition(self):
        pass

    def getWord(self):
        return self.word

    def setWord(self, word):
        self.word = word
