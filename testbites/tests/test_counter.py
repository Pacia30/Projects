from lib.counter import*

def test_counter_to_five():
    count_to_five = Counter()
    count_to_five.add(5)
    result = count_to_five.report()
    assert result == "Counted to 5 so far."

def test_counter_to_eight():
    count_to_eight = Counter()
    count_to_eight.add(8)
    result = count_to_eight.report()
    assert result == "Counted to 8 so far."