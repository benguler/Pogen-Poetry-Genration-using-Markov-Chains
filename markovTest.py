import random
import string
from string import ascii_lowercase

def markov(words, probs, seed):
    phrase = ""

    seed = seed

    for i in range(5):
        phrase += seed + " "
        
        index = words.index(seed)

        prevProb = 0.0

        for j in range(len(words)):
            rando = random.uniform(0, 1)
            
            if(probs[index][j]) >=rando or (probs[index][j] + prevProb) >= 0.999999999999:
               seed = words[j]

               break

            prevProb += probs[index][j]

        prevProb = 0.0

        lastWord = seed
        
    return (phrase, lastWord)

poetry = open("./Poems.txt", "r", encoding = "utf8")
words = open("./Words.txt", "w", encoding = "utf8")

word = ""

wordList = []
probs = []

alphabet = list(ascii_lowercase)

wordList = []
numOfWord = []
probs = []

prevWord = ""

for l in poetry.read().splitlines():
    for c in l:
        if c.lower() in alphabet:
           word += c.lower()

        if c == " " and word != "":
            words.write(word)
            prevWord = word

            words.write("\n")
            word = ""

    if word != "":
        words.write(word)
        prevWord = word

        words.write("\n")
        word = ""

words = open("./Words.txt", "r", encoding = "utf8")

for w in words.read().splitlines():
        
    if w not in wordList:
        wordList += [w]

    if len(wordList) > len(numOfWord):
       numOfWord += [1]
       
    else:
        numOfWord[wordList.index(w)] += 1

for i in range(len(wordList)):
    probs += [[]]
    
    for j in range(len(wordList)):
        probs[i] += [0.0]

prevWord = ""

words = open("./Words.txt", "r", encoding = "utf8")

for w in words.read().splitlines():
    if prevWord != "":
        probs[wordList.index(prevWord)][wordList.index(w)] += 1/numOfWord[wordList.index(prevWord)]
        
    prevWord = w


a = ""

while True:
    print("Enter the first word of your poem, or 'N' to exit:")

    a = input()

    if a[0].lower() == "n" and len(a) == 1:
        print("BYE")
        break

    seed = a

    print("----------------------------------------------------\n")
    
    for i in range(3):
        result = markov(wordList, probs, seed)
        
        print(result[0])
        print("\n")
        seed = result[1]

    print("----------------------------------------------------")
