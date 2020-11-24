import random
import sys

BEGIN = "___BEGIN__"
END = "___END__"


class MarkovMatrix:
    def __init__(self, corpus, state_size, matrix=None):
        self.corpus = corpus
        self.state_size = state_size
        self.matrix = {}

    def train(self, corpus, state_size):
        for token in self.corpus:
            key = ([ BEGIN ] * state_size) + key + [ END ]
            for i in range(len(token) + 1):
                state = tuple(key[i:i + state_size])
                follow = key[i + state_size]
                if state not in self.matrix:
                    self.matrix[state] = {}

                if follow not in self.matrix[state]:
                    self.matrix[state][follow] = 0

                self.matrix[state][follow] += 1

    def get_matrix(self):
        return self.matrix