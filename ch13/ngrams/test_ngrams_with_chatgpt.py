
import unittest
import re

# Assume the functions are defined in the same file or imported from another module
def lowercase_remove_punct_numbers(text, supercharte=True):
    return re.sub(r'[^a-z\s]', '', text.lower())

def multiple_to_single_spaces(text):
    return re.sub(r'\s+', ' ', text)

def create_ngrams(text, n, supercharge, tests) -> list:
    processed_text = lowercase_remove_punct_numbers(text)
    single_space_processed = multiple_to_single_spaces(processed_text)
    return [single_space_processed[i:i+n] for i in range(len(single_space_processed)-n+1)]


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
            create_ngrams(text, 7, supercharge=True, tests=True),
            expected_ngrams
        )

    def test_create_ngrams_short_input(self):
        text = "Hi"
        self.assertEqual(
            create_ngrams(text, 5, supercharge=True, tests=True),
            []
        )

    def test_create_ngrams_multiple_spaces(self):
        text = "Hello     world"
        expected_ngrams = ['hello w', 'ello wo', 'llo wor', 'lo worl', 'o world']
        self.assertEqual(
            create_ngrams(text, 7, supercharge=True, tests=True),
            expected_ngrams
        )


class TestTextUtilsAdditional(unittest.TestCase):

    def test_lowercase_remove_punct_numbers_empty_string(self):
        self.assertEqual(lowercase_remove_punct_numbers(""), "")

    def test_lowercase_remove_punct_numbers_only_punct_and_numbers(self):
        self.assertEqual(lowercase_remove_punct_numbers("1234!@#$%^&*()"), "")

    def test_lowercase_remove_punct_numbers_only_alpha(self):
        self.assertEqual(lowercase_remove_punct_numbers("ABCdef"), "abcdef")

    def test_lowercase_remove_punct_numbers_whitespace_mix(self):
        self.assertEqual(lowercase_remove_punct_numbers("ABC\tDEF\nGHI"), "abc\tdef\nghi")

    def test_multiple_to_single_spaces_empty_string(self):
        self.assertEqual(multiple_to_single_spaces(""), "")

    def test_multiple_to_single_spaces_only_whitespace(self):
        self.assertEqual(multiple_to_single_spaces("   \t  \n "), " ")

    def test_multiple_to_single_spaces_already_single(self):
        self.assertEqual(multiple_to_single_spaces("This is fine"), "This is fine")

    def test_create_ngrams_empty_text(self):
        self.assertEqual(create_ngrams("", 3, supercharge=True, tests=True), [])

    def test_create_ngrams_n_larger_than_text(self):
        self.assertEqual(create_ngrams("Hi", 10, supercharge=True, tests=True), [])

    def test_create_ngrams_n_equal_to_text_length(self):
        self.assertEqual(create_ngrams("Hello", 5, supercharge=True, tests=True), ["hello"])

    def test_create_ngrams_non_alpha_with_spacing(self):
        self.assertEqual(
            create_ngrams("### Hello --- there!!", 5, supercharge=True, tests=True),
            [" hell", "hello", "ello ", "llo t", "lo th", "o the", " ther", "there"]
        )

    def test_create_ngrams_large_n(self):
        self.assertEqual(create_ngrams("hello world", 50, supercharge=True, tests=True), [])


if __name__ == '__main__':
    unittest.main()
