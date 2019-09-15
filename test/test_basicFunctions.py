import pytest
import src.basicFunctions as f

'''
From here on out we'll be using functions to run our code. Functions allow us to reuse code so we don't repeat ourselves
Functions can return a value that you can assign to a variable.
If the function does not return a value it is a void function and can be tested in other ways beside an assert
'''

def test_getsHelloWorld():
    # you call a function by typing its name with parens
    # see the import on line 2. This is bringing in the code in the src.functions file
    # you can use it by typing f. this will bring up a list of available functions
    # Assign the helloWorld function to the response variable

    response = None
    assert response == "Hello, World!"


def test_getHelloWorldWithName():
    # Functions can sometimes be called with arguments(values that you pass into the function)
    # this makes them more useful
    # call the helloWorldWithNameFunction with the name Annie
    # Arguments go inside the ()

    response = None

    assert response == "Hello, Annie!"


def test_addReturnsNine():
    # call with add function with two integer numbers that sum to nine
    # You will need to write the entire add function yourself. It will need to accept two numbers
    response = None

    assert response == 9

