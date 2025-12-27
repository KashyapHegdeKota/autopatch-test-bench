import pytest
from math_engine import calculate_average

def test_standard_list():
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_empty_list():
    print("Testing with an empty list to check for ZeroDivisionError.")
    assert calculate_average([]) == 0  # Expecting the function to handle empty list gracefully