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
        with open('lst.txt') as f:
            words = [word.strip().lower() for word in f.readlines()]

    def get_anagrams(self, word):
        """ list comprehension / itertools permutation """
        return [w for w in anagram(word) if w in self.words_list]

def anagram(word):
    for w in itertools.permutations(word):
        yield ''.join(w)