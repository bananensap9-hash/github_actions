import pytest


def test_calc_addition():
    output = 2 + 4
    assert output == 6


def test_calc_substraction():
    # Test subtraction result of 2-4
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    # Test multiplication result of 2*4
    output = 2 * 4
    assert output == 8


def test_coucou():
    # Test if result returns 'hello'
    output = 'hello'
    assert output == 'hello'
