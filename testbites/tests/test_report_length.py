from lib.report_length import *

def test_report_length_ippo():
    word = report_length('ippo')
    assert word == "This string was 4 characters long."