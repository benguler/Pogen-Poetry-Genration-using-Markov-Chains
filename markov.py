import random
import sys

BEGIN = "___BEGIN__"
END = "___END__"


class MarkovMatrix:
    def __init__(self, corpus, state_size, matrix=None):
        self.corpus = corpus
        self.state_size = state_size
        self.matrix = {}
        self.train(corpus, state_size)

    def train(self, corpus, state_size):
        for token in self.corpus:
            key = ([ BEGIN ] * state_size) + token + [ END ]
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
    
# Example Usage

text = [["Farewell", "dear", "mate,", "dear", "love!"],
        ["I’m", "going", "away,", "I", "know", "not", "where"]]

m = MarkovMatrix(text, 2)
matrix = m.get_matrix()

for item in matrix:
    print(item, end= ' = ')
    print(matrix[item])

print(matrix[("Farewell", "dear")])
