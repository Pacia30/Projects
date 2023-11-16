from lib.extract_uppercase_words import extract_uppercase_words

def test_with_empty_string():
    assert extract_uppercase_words("") ==[]

def test_with_lowercase_words():
    assert extract_uppercase_words('hello my name ippo') ==[]