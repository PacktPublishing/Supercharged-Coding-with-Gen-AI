import re

def lowercase_remove_punct_numbers(text, supercharte=True):
    return re.sub(r'[^a-z\s]', '', text.lower())

def multiple_to_single_spaces(text):
    letters_single_spaces = re.sub(r'\s+', ' ', text)
    return letters_single_spaces

def create_ngrams(text, n) -> list:
    '''create a list of n-gram tuples from the input text.'''
    processed_text = lowercase_remove_punct_numbers(text)
    single_space_processed = multiple_to_single_spaces(processed_text)
    u = [single_space_processed[i:i+n] for i in range(len(single_space_processed)-n+1)]
    return u

if __name__ == "__main__":
    text = "This is a sample text $ABC% for creating n-grams."
    n = 3
    print(create_ngrams(text, n))