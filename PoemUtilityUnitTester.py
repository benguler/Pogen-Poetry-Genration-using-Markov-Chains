'''
PoemUtilityUnitTester.py

Contributors - Alex Castro

A simple test class for testing all methods of PoemUtility.py.

'''

import unittest
from PoemUtility import *


class PoemUtilityUnitTester(unittest.TestCase):
    
    # def test_tokenize(self):
    #     filename = 'test.csv'
    #     #some_matrix
    #     PoemUtility.tokenize(filename)
    #     #print(some_matrix)


    # def test_tokenize_exception(self):
    #     filename = 'some_file_from_another_world'
    #     self.assertRaises(Exception, PoemUtility.tokenize(filename))
            

    def test_classifyPoems(self):
        filename = 'all_200.csv'
        PoemUtility.classifyPoems(filename)


    # def test_classifyPoems_exception(self):
    #     filename = 'mooooodern_loooove.csv'
    #     self.assertRaises(Exception, PoemUtility.classifyPoems(filename))

    
    def test_classifySentence(self):
        sentence = 'He caught me running with Lucius Atherton'
        category = 'modern_love'
        result = PoemUtility.classifySentence(sentence, category)
        print(result)
          

        
if __name__ == '__main__':
    unittest.main()