

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