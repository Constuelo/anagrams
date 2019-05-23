# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Thread Safe implementation
#   - Write more tests

import unittest
import time

"""
This code is written in python 3.7.2

- DeprecationWarnings ignored
- ResourceWarnings ignored

- Optimise results (anagrams.get_anagrams('petals'))
    - sorted() = ~0.06-0.08 secs
    - Itertools permutation = ~0.45-0.5 secs

- thread safe operations
    - sorted() - yes
    - list comprehension - yes
    - open() - yes
"""

class Anagrams:

    def __init__(self):
        self.words = open('words.txt').readlines()
        self.words_list = self.words_to_list()

    def words_to_list(self):
        """ Creates a copies of self.words and strips the newlines
            :rtype: list
        """
        return [word.strip('\n') for word in self.words]

    def get_anagrams(self, word):
        """ Returns all anagrams from self.words_list for a given word.
            :param: word
            :ptype: str
            :rtype: list
        """
        if isinstance(word, str):
            return [a for a in self.words_list if sorted(word.lower()) == sorted(a.lower())]
        else:
            print(f'{word} is not a str')


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
