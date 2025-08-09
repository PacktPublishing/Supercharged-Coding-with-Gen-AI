import unittest
from ngrams import lowercase_remove_punct_numbers

class TestLowercaseRemovePunctNumbers(unittest.TestCase):

    def test_basic_case(self):
        text = "Hello, World! 123"
        result = lowercase_remove_punct_numbers(text)
        self.assertEqual(result, "hello world")

    def test_with_special_characters(self):
        text = "Python@3.9 is #1!"
        result = lowercase_remove_punct_numbers(text)
        self.assertEqual(result, "python is ")

    def test_empty_string(self):
        text = ""
        result = lowercase_remove_punct_numbers(text)
        self.assertEqual(result, "")

    def test_only_numbers_and_punctuation(self):
        text = "12345!@#$%"
        result = lowercase_remove_punct_numbers(text)
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
