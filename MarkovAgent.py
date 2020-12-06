import random
from markov import MarkovMatrix

class MarkovAgent:
    def __init__(self, markov, initState):
        self.markov = markov
        self.state = initState
        self.markov = markov
        self.stateSize = markov.state_size
    
    def transition(self):
        newState = self.state[1:self.stateSize] + (self.markov.move(self.state), )
    
        self.state = newState
        
    def getState(self):
        return self.state
        
    def setState(self, state):
        self.state = state
        
    