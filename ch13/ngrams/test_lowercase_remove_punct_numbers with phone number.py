import unittest
from src.ngrams import lowercase_remove_punct_numbers

# File: test_ngrams.py

class TestLowercaseRemovePunctNumbers(unittest.TestCase):
    def test_mixed_input(self):
        text = "Hello, World! 123"
        expected = "hello world"
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_lowercase_only(self):
        text = "this is a test"
        expected = "this is a test"
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_punctuation_and_numbers(self):
        text = "!@#$%^&*()1234567890"
        expected = ""
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_empty_string(self):
        text = ""
        expected = ""
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)

    def test_spaces_and_special_characters(self):
        text = "   Hello!!   World??   "
        expected = "   hello   world   "
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)
        
    def test_phone_number(self):
        text = "Call me at 123-456-7890."
        expected = "call me at"
        self.assertEqual(lowercase_remove_punct_numbers(text), expected)
        
if __name__ == "__main__":
    unittest.main()