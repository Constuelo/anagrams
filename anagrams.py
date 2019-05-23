# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval
#   - Thread Safe implementation
#   - Write more tests

import unittest
import itertools
import time

"""
- Optimise the code for fast retrieval
    - Look at algorithms

- Optimise results (anagrams.get_anagrams('petals'))
     - sorted() = ~0.06-0.07 secs
     - Itertools permutation = ~0.45-0.5 secs

- thread safe operations
     - sorted() - yes
     - list comprehension - yes
"""

class Anagrams:

    def __init__(self):
        self.words = open('words.txt', 'r').readlines()
        self.words_list = self.words_to_list()

    def words_to_list(self):
        return [word.strip().lower() for word in self.words]

    def get_anagrams(self, word):
        return [a for a in self.words_list if sorted(word) == sorted(a)]


if __name__ == '__main__':
    start = time.time()
    anagrams = Anagrams()
    print(anagrams.get_anagrams('petals'))  # ['palest', 'pastel', 'petals', 'plates', 'staple']
    print(f'\nValidation took {float("%0.2f" % (time.time() - start))} seconds to run')




#     def get_anagrams(self, word):
#         """ list comprehension / itertools permutation """
#         return [w for w in anagram(word) if w in self.words_list]

# def anagram(word):
#     for w in itertools.permutations(word):
#         yield ''.join(w)