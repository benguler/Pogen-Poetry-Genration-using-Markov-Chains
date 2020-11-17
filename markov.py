import random
import sys


class MarkovMatrix:
    def __init__(self, training_data):
        self.data = {}
        self.training_data = training_data
        self.prev = ''

    def train(self):
        prev = ""
        for token in self.training_data:
            token = sys.intern(token)
            if not prev in self.data:
                self.data[prev] = [0, {}]

            if not token in self.data[prev][1]:
                self.data[prev][1][token] = 0

            self.data[prev][1][token] += 1
            self.data[prev][0] += 1

            prev = token

    def get_matrix(self):
        return self.data

    def selectToken(self, state=None):
        if state is None:
            state = self.prev
        if not state in self.data:
            self.data[state] = 0
        self.data[state] += 1
        return self._choose(self.data[state])

    def choose(self, freqdict):
        total, choices = freqdict
        idx = random.randrange(total)

        for token, freq in choices.items():
            if idx <= freq:
                return token

            idx -= freq
