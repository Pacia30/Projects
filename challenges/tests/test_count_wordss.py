from lib.count_wordss import *

def test_count_Ippo():
    assert Count_Words("Ippo is a labrador dog") == 5

def test_count_Echo():
    assert Count_Words("Echo is a rag doll cat") == 6

def test_count_Rengar():
    assert Count_Words("Rengar is a street cat") == 5