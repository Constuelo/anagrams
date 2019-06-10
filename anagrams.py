# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Thread Safe implementation
#   - Write more tests

import unittest


class Anagrams:
    
    def __init__(self):
        with open('words.txt') as reader:
            self.words = reader.readlines()
        self.words_list = [word.strip('\n') for word in self.words]

    def get_anagrams(self, word):
        return [a for a in self.words_list if sorted(word.lower()) == sorted(a.lower())]


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('plates'), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    def test_lowercase_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    def test_sentencecase_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('Keats'), ['Keats', 'skate', 'stake', 'steak', 'takes'])

    def test_uppercase_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('MITRE'), ['merit', 'miter', 'MITRE', 'remit', 'timer'])

    def test_mixedcase_anagrams(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('MicroVAX'), ['MicroVAX'])

    def test_alphanumeric(self):
        anagrams = Anagrams()
        self.assertEquals(anagrams.get_anagrams('Modula-2'), ['Modula-2'])


if __name__ == '__main__':
    unittest.main()
