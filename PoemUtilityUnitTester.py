'''
PoemUtilityUnitTester.py

Contributors - Alex Castro

A simple test class for testing all methods of PoemUtility.py.

'''

import unittest
from PoemUtility import *


class PoemUtilityUnitTester(unittest.TestCase):
    
    def test_classifyPoems(self):
        filename = 'test.csv'
        PoemUtility.classifyPoems(self,filename)
        
        
    def test_tokenize(self):
        filename = 'test.csv'
        PoemUtility.tokenize(filename)
        #print(some_matrix)
        
        
    def test_classifySentence(self):
        sentence = 'He caught me running with Lucius Atherton'
        category = 'modern_love'
        result = PoemUtility.classifySentence(self, sentence, category)
        print(result)
        
        
    def test_tokenize_exception(self):
        filename = 'some_file_from_another_world'
        self.assertRaises(Exception, PoemUtility.tokenize(filename))
        
        
    def test_classifyPoems_exception(self):
        filename = 'mooooodern_loooove.csv'
        self.assertRaises(Exception, PoemUtility.classifyPoems(self, filename))
        
        
if __name__ == '__main__':
    unittest.main()