from real_intermediate_test_app import very_complex_logic
from time import sleep


def test_complex_logic_slow_1():
    sleep(1)
    assert very_complex_logic(1, 2, 3) == 6
