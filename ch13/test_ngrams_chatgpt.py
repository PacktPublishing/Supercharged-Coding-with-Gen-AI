import unittest
from src.ngrams import lowercase_remove_punct_numbers, multiple_to_single_spaces, create_ngrams

class TestTextUtils(unittest.TestCase):

    def test_lowercase_remove_punct_numbers_basic(self):
        self.assertEqual(
            lowercase_remove_punct_numbers("Hello, WORLD!123"),
            "hello world"
        )

    def test_lowercase_remove_punct_numbers_with_symbols(self):
        self.assertEqual(
            lowercase_remove_punct_numbers("Te$ting #punctu@ation &numbers 456"),
            "testing punctuation numbers "
        )

    def test_multiple_to_single_spaces_basic(self):
        self.assertEqual(
            multiple_to_single_spaces("This   is   a    test"),
            "This is a test"
        )

    def test_multiple_to_single_spaces_with_tabs_and_newlines(self):
        self.assertEqual(
            multiple_to_single_spaces("Line1\nLine2\tLine3   Line4"),
            "Line1 Line2 Line3 Line4"
        )

    def test_create_ngrams_basic(self):
        text = "Hello, world!"
        expected_ngrams = ['hello w', 'ello wo', 'llo wor', 'lo worl', 'o world']
        self.assertEqual(
            create_ngrams(text, 7),
            expected_ngrams
        )

    def test_create_ngrams_short_input(self):
        text = "Hi"
        self.assertEqual(
            create_ngrams(text, 5),
            []
        )

    def test_create_ngrams_multiple_spaces(self):
        text = "Hello     world"
        expected_ngrams = ['hello w', 'ello wo', 'llo wor', 'lo worl', 'o world']
        self.assertEqual(
            create_ngrams(text, 7),
            expected_ngrams
        )

if __name__ == '__main__':
    unittest.main()
