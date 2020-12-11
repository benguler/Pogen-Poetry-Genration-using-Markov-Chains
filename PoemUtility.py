"""
PoemUtility.py
Contributors - Alex Castro

This python script contains three important functionality

1- Opens a csv file for reading and uses TextBlob to tokenize each sentence into a nested list of words

2- Classify poems using the TextBlob Naive-Bayes classifier.

3- Calculate the probability distance that the sentence belongs to the given poem category



"""

import csv
from textblob import TextBlob
#from textblob.classifiers import NaiveBayesClassifier

#according to StackOverflow use the classifiers.py is faster in training and classifying
from classifiers import NaiveBayesClassifier


class PoemUtility:

    @staticmethod
    def tokenize(self, filename):
        try:
            matrix = []
            with open ('CSVs/processed/'+filename, 'r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                data_lines = list(csv_reader)

                for line in data_lines:
                    poem_sentence = TextBlob(line['poem_line'])
                    mystr = poem_sentence.words
                    matrix.append(mystr)
            return matrix
        except IOError:
            print ('\nFile not found in tokenize() method')
    
    
    @staticmethod
    def classifyPoems(self, filename):
        try:
            with open('CSVs/processed/'+filename, 'r') as fp:
                print('opened ' + filename )
                global cl
                cl = NaiveBayesClassifier(fp, format="csv")
                print(cl)
        except IOError:
            print('\nFile not found for Naive-Bayes Classifier')
            

    @staticmethod
    def classifySentence(self, sentence, category):
        prob_dist = cl.prob_classify(sentence)
        return round(prob_dist.prob(category),2)
                
        