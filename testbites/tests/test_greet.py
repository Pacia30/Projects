from lib.greet import *

def test_greet_sammy():
    hello = greet('Sammy')
    assert hello == "Hello, Sammy!"

def test_greet_ippo():
    hello = greet('Ippo')
    assert hello == "Hello, Ippo!"