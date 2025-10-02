import pytest # pyright: ignore[reportMissingImports]
import Functions

def test_add():
    assert Functions.add(4,9) == 13
    assert Functions.add(-3,-4) == -7

def test_subtract():
    assert Functions.subtract(5,1) == 4
    assert Functions.subtract(-100,-2) == -98

def test_multiply():
    assert Functions.multiply(3,22) == 66
    assert Functions.multiply(-3,-4) == 12

def test_divide():
    assert Functions.divide(8,2) == 4
    assert Functions.divide(10,-4) == -2.5

def test_mod():
    assert Functions.mod(25,4) == 1
    assert Functions.mod(-4,100) == 96

def test_exponent():
    assert Functions.exponent(2,8) == 256
    assert Functions.exponent(100,3) == 1000000

def test_factorial():
    try:
        assert Functions.factorial(-2) < 0, "Should return a negative value message\n"
    except AssertionError as err:
        print(err)

    try:
        assert Functions.factorial(0) == 1, "Result should equal 1\n"
    except AssertionError as err:
        print(err)
        
    try:
        assert Functions.factorial(5) == 120, "Result should equal 120"
    except AssertionError as err:
        print(err)