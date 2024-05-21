import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(3,4)
    assert result == 7
    
def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5
    
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):       
        result = my_functions.divide(5, 0)
    assert True              #! we are asserting 'True'. because by calling this function, the exception should be raised