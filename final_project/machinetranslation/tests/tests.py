import unittest
import os
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory to the sys path
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

from translator import english_to_french , french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("None"), '') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
       

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("None"), '') 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        

unittest.main()