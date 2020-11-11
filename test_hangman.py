import unittest
import hangman


class Tester(unittest.TestCase):

    def test_valid_reveal(self):
        word = "United States of America"
        revealed_word = ['_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', '_', '_', ' ', '_', '_', ' ', '_', '_', '_', '_', '_', '_', '_']
        result = hangman.reveal('a', revealed_word, word)
        self.assertEqual(result, ['_', '_', '_', '_', '_', '_', ' ', '_', '_', 'a', '_', '_', '_', ' ', '_', '_', ' ', 'A', '_', '_', '_', '_', '_', 'a'])

    def test_valid_reveal_shorter_word(self):
        word = "United States"
        revealed_word = ['_', '_', '_', '_', '_', '_', ' ', '_', '_', '_', '_', '_', '_']
        result = hangman.reveal('a', revealed_word, word)
        self.assertEqual(result, ['_', '_', '_', '_', '_', '_', ' ', '_', '_', 'a', '_', '_', '_'])
    
    def test_valid_reveal_empty_word(self):
        word = ""
        revealed_word = []
        result = hangman.reveal('a', revealed_word, word)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()