"""Perform tests of the fizz_buzz function"""


import pytest

from fizzbuzz import fizz_buzz

inputs = [3, 5, 15, 4, 10, 115, 7]

outputs = ["fizz", "buzz", "fizzbuzz", "4", "buzz", "buzz", "7"]


@pytest.mark.paramterize("inp,out", zip(inputs, outputs))
def test_fizzbuzz(inp, out):
    """
    Takes inputs, gets the output o fthe fizzbuzz function.
    Asserts whether equality holds.
    """
    assert fizz_buzz(inp) == out
