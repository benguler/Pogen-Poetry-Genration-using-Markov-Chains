"""
poem_tokenizer.py
Contributors: Alex Castro

This python script opens a csv file for reading and uses TextBlob to tokenize a sentence into a list of words
Moreover, the set is cast into a list for later usability


Possible Improvements: Export distinct words found in poems into a CSV file 

"""

import csv
from textblob import TextBlob


class PoemTokenizer():
    
    def tokenize(filename):
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
            print('file not found')
            
            
            
'''
 - concatenate all csv files
 - Add texxt blob classification to this file (a function that takes string, category)
   and return the probability distance
   
 - train the csv file inside the constructor


'''
                
              

