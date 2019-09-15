import pytest


def test_assignStringVariable():
    # assign a string variable called greeting to the value of Hello, world!
    greeting = "No U"

    assert greeting == "Hello, world!"


def test_assignNumberVariable():
    # assign a number variable called number to the value of 18
    number = 1000

    assert number == 18

def test_assignDecimalVariable():
    # assign a number variable called number to the value of 3.14
    decimal = 1000

    assert decimal == 3.14

def test_decimalsAndIntegersAreNotTheSame():
    # fix the decimal and interger variables
    decimal = 1000
    integer = "I am an integer"

    assert isinstance(decimal, float)
    assert isinstance(integer, int)



def test_addStringsTogether():
    # assign a string variable called greeting to the value of Hello, Lucy!
    # Remember that the computer isn't smart enough to add spaces on its own, you need to include them
    # This is called string concatenation
    greeting = "No U"
    name = "today"

    assert (greeting + name) == "Hello, Lucy!"


def test_addIntegersTogether():
    # adding integers together is pretty easy. Make int1 and int2 add to 7
    int1 = 1
    int2 = 2

    total = int1 + int2
    assert total == 7


def test_addIntegersToDecimalsTogether():
    # adding integers together is pretty easy. Make int1 and int2 add to 7
    # whenever you add a integer to a decimal the resulting number becomes a decimal
    # technically it's a floating point integer or float
    integer = 1
    decimal = 2

    total = integer + decimal
    assert total == 7.0
    assert isinstance(total, float)


def test_addFloatsTogether():
    # adding floats together seems like it should be easy, but it is hard
    # This is something of a trick test as there is only one combination of float1 and float2 that will pass
    # Computers are not very smart with decimals and they frequently make math errors with them
    # There are math modules in python that will fix this issue, but we won't cover them just yet
    # try different combinations and see
    # to pass the test you need to set the numbers to 0.0 and 3.3, which really isn't adding anything
    float1 = 1.0
    float2 = 2.0

    total = float1 + float2
    assert total == 3.3
