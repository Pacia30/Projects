from lib.check_codeword import *

def test_check_code_word_horse():
    code = check_codeword('horse')
    assert code == "Correct! Come in."

def test_check_code_word_home():
    code = check_codeword('home')
    assert code == "Close, but nope."

def test_check_code_word_ippo():
    code = check_codeword('ippo')
    assert code == "WRONG!"
