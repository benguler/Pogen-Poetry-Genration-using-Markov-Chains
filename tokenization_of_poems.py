"""
tokenization_of_poems.py
Contributors: Alex Castro

This python script opens a csv file for reading and uses TextBlob to tokenize words into a set
Moreover, the set is cast into a list for later usability


Possible Improvements: Export distinct words found in poems into a CSV file 

"""

from textblob import TextBlob
import csv
data = open('all.csv', encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

word_set = set()


for line in data_lines:
    poem_line = TextBlob(line[1])
    for s in poem_line.words:
        if (len(s) > 1):
            word_set.add(s)


word_list = list(word_set)
#print(word_list[1])
#print(word_list[0])



