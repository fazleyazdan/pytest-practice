import time
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
    
    
#* ********* Using Mark & Parameters ********** *#

#* Mark is the same as 'tags' in cypress. i.e (skip, only)

# if the test case execute slow then we can mark it as slow

@pytest.mark.slow
def test_add_slow():
    time.sleep(5)
    assert my_functions.add(3, 4) == 7
    

@pytest.mark.skip(reason= 'this test case already executed hence skipping')
def test_add_skip():
    assert my_functions.add(3, 4) == 7

@pytest.mark.xfail(reason='we know that this test case is going to fail')      #! you can also add reason for explanation 
def test_zero_division():
    my_functions.divide(4,0)
    
# for skipped test case 's' & for xfail 'x' will be shown. in our case the first 4 cases passed, the fifth skipped and the last failed.
#* in terminal it will be shown like this:    ....sx

