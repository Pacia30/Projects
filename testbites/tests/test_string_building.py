from lib.string_builder import *

def test_string_build_ippo():
    string_ippo = StringBuilder()
    string_ippo.add('Ippo')
    assert string_ippo.output() == 'Ippo'

def test_string_size_ippo_echo():
    string_ippoecho = StringBuilder()
    string_ippoecho.add('Ippo.')
    string_ippoecho.add('Echo')
    assert string_ippoecho.size() == 9