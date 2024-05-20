import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(3,4)
    assert result == 7
    
def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5