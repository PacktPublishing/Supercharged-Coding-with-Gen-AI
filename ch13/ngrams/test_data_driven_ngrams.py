import unittest 

from ngrams import lowercase_remove_punct_numbers 

 
class TestLowercaseRemovePunctNumbers(unittest.TestCase): 
    def test_data_driven(self): 
        test_cases = [ 

            # (input, expected_output) 
            ("Hello, World! 123", "hello world "), 
            ("ABCdef", "abcdef"), 
            ("1234!@#$", ""), 
            ("A1! b2@ C3#", "a b c"), 
            ("", ""), 
            (" ", " "), 
            ("Python3.8_is#aweSome!", "pythonisawesome"), 
            ("No PUNCTUATION", "no punctuation"), 
            ("MiXeD CaSe &*^%", "mixed case "), 
            ("newline\nTab\tSpace ", "newline\ttab\tspace "), 
        ]
        for input_text, expected in test_cases: 
            with self.subTest(input=input_text): 
                self.assertEqual(lowercase_remove_punct_numbers(input_text), expected) 

if __name__ == "__main__":
    unittest.main()