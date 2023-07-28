from sum import calculate


def test_sum(name):
    n = calculate(2, 3)
    print(name)
    assert n == 5, 'n != 5'

