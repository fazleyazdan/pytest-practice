import pytest
import source.shapes as shapes

def test_area():
    rectangle = shapes.Rectangle(7, 3)
    assert rectangle.area() == 7 * 3
    
def test_perimeter():
    rectangle = shapes.Rectangle(7, 3)
    assert rectangle.perimeter() == 7 * 2 + 3 * 2


#* ************************************************* *#

#! Now as you can see the statement, 'rectangle = shapes.Rectangle(7, 3)' is repeated multiple time in the above code
#! we can avoid it by using fixture in pytest

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(7,3)

def test_area_fix(my_rectangle):              #* here we have passed my_rectangle() method as a parameter
    assert my_rectangle.area() == 7 * 3       #* called area() function with the fixture method 
    
def test_perimeter_fix(my_rectangle):          
    assert my_rectangle.perimeter() == 7 * 2 + 3 * 2 

    
#! if you want to use the fixture globally, then we have to keep the fixture content inside the 'conftest.py' file.
#! see the test 'test_conftest.py' for more detail
