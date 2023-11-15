from lib.snippet import *

def test_Ippo_Makunouchi():
    word = make_snippet("IppoMakunouchi")
    assert word == "IppoM..."

# not needing to create a "word"

def test_echo():
    assert make_snippet("Echo") == "Echo"