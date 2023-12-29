# Save this file as test_factorial.py

import pytest
from your_factorial_module import factorial

# Assuming your_factorial_module contains the factorial function

def test_factorial_positive_integer():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_negative_number():
    with pytest.raises(ValueError):
        factorial(-5)

def test_factorial_boundary_value():
    # Testing the behavior change at a boundary value
    assert factorial(12) == 479001600
    assert factorial(13) == 6227020800
