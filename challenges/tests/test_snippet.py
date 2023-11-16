from lib.snippet import *

def test_Ippo_Makunouchi():
    word = make_snippet("Ippo Makunouchi")
    assert word == "Ippo Makunouchi"

# not needing to create a "word"

def test_echo():
    assert make_snippet("Echo") == "Echo"

def test_Ippo():
    assert make_snippet("Ippo is a four legged dog") == "Ippo is a four legged..."