import unittest
from ngrams import lowercase_remove_punct_numbers, multiple_to_single_spaces, create_ngrams

class TestNgramsFunctions(unittest.TestCase):

    def test_lowercase_remove_punct_numbers(self):
        text = "Hello, World! 123"
        result = lowercase_remove_punct_numbers(text)
        self.assertEqual(result, "hello world")

    def test_lowercase_remove_punct_numbers_with_supercharte(self):
        text = "Python@3.9 is #1!"
        result = lowercase_remove_punct_numbers(text, supercharte=True)
        self.assertEqual(result, "python is ")

    def test_multiple_to_single_spaces(self):
        text = "This   is  a   test"
        result = multiple_to_single_spaces(text)
        self.assertEqual(result, "This is a test")

    def test_create_ngrams(self):
        text = "This is a test"
        n = 2
        result = create_ngrams(text, n)
        expected = ["Th", "hi", "is", " s", "is", " a", "a ", " t", "te", "es", "st"]
        self.assertEqual(result, expected)


class TestLowercaseRemovePunctNumbers(unittest.TestCase):

    def test_basic_text(self):
        text = "Hello, World!"
        expected = "hello world"
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_text_with_numbers(self):
        text = "Python 3.9 is awesome!"
        expected = "python  is awesome"
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_text_with_special_characters(self):
        text = "@#AI&ML* are cool!"
        expected = "ai ml are cool"
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_empty_string(self):
        text = ""
        expected = ""
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_only_special_characters(self):
        text = "!@#$%^&*()"
        expected = ""
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

if __name__ == "__main__":
    unittest.main()
