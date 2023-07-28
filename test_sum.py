from sum import calculate
import logging




def test_sum(name):
    n = calculate(2, 3)
    # print(name)
    logging.error('Error')
    assert n == 3, 'n != 5'
