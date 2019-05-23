# pylint: disable=R0903, C0111
from operator import itemgetter
from collections import Counter, defaultdict
import unittest
import logging
import time



class WordNotFoundError(KeyError):
    """
    Error raised when word not in anagram list
    """


class Anagrams:
    """
    Class provides anagrams of a given word.
    Keyword arguments:
    strict_mode (boolean) -- enable error raising mode (default False)
    Limitations - if a valid word exists, but is not in the list,
    it will not be recognised as potential anagram.
    This is for performance reasons, as well as unspecified
    behaviour concerning unknown words.
    This only uses threadsafe objects, so will be threadsafe.
    """
    def __init__(self, strict_mode=False):
        self.strict_mode = strict_mode

        # Load in words, and strip whitespace characters
        with open('words.txt') as words_file:
            words = [word.strip().lower() for word in words_file.readlines()]

        # Produce the maps of word to counters, and counters to words
        input_word_map = {}
        reverse_map = defaultdict(list)
        counters = []
        for word in words:
            counter_list = list(Counter(word).items())
            counter_list.sort(key=itemgetter(0))
            counter_tuple = tuple(counter_list)
            counters.append(counter_tuple)
            input_word_map[word] = counter_tuple
            reverse_map[counter_tuple].append(word)

        # Connect up words to their anagrams
        self.anagram_map = {}
        for word, counter in input_word_map.items():
            anagram_list = reverse_map[counter]
            anagram_list.sort()
            self.anagram_map[word] = anagram_list

    def get_anagrams(self, word):
        """
        Get the anagrams of a given word.
        Keyword arguments
        word - word you are trying to find anagrams for (case insensitive)
        If strict mode is off (default), then if a word isn't found
        it'll return a list with that word in, and raise a logging warning.
        If strict mode is on, then if a word isn't found a WordNotFoundError
        is raise.
        """
        lower_word = word.lower()
        if lower_word in self.anagram_map:
            return self.anagram_map[lower_word]
        if self.strict_mode:
            raise WordNotFoundError("{} not found".format(lower_word))
        else:
            logging.warning(
                "%s was not found in the list of words", lower_word)
            return [lower_word]


class TestAnagrams(unittest.TestCase):
    """
    Test Anagrams class functionality"
    """

    def test_lower_case_anagrams(self):
        """
        Ensure that default functionality, that the anagram is returned.
        """
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('plates'), [
            'palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(
            anagrams.get_anagrams('eat'), ['ate', 'eat', 'tea'])

    def test_mixed_case_anagrams(self):
        """
        Check that mixed case words still work.
        """
        anagrams = Anagrams()
        self.assertEqual(anagrams.get_anagrams('peTAls'), [
            'palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(
            anagrams.get_anagrams('EaT'), ['ate', 'eat', 'tea'])

    def test_input_is_in_output(self):
        """
        Check that the input word is found in the output list
        """
        anagrams = Anagrams()
        self.assertIn('petals', anagrams.get_anagrams('petals'))
        self.assertIn('abide', anagrams.get_anagrams('abide'))

    def test_strict_mode_input_not_in_word_list(self):
        """
        Test that in strict mode, a word not in the list
        raises a WordNotFoundError
        """
        anagrams = Anagrams(strict_mode=True)
        with self.assertRaises(WordNotFoundError):
            anagrams.get_anagrams("cheeseburger")

    def test_default_mode_input_not_in_word_list(self):
        """
        Test that in default (non-strict mode) a warning is raised
        and the word is returned as a single item in a list.
        """
        anagrams = Anagrams()
        with self.assertLogs(level="WARNING") as logging_capture:
            self.assertEqual(
                anagrams.get_anagrams('cheeseburger'),
                ['cheeseburger']
            )
        self.assertEqual(
            logging_capture.output, [
                'WARNING:root:cheeseburger was not found in the list of words']
            )

if __name__ == '__main__':
    # unittest.main()
    anagram = Anagrams()
    print(anagram.get_anagrams('petal'))