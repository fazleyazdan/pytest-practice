import pytest
import source.shapes as shapes

#* using content from conftest.
#* in the below example 'my_rectangle' is used from 'conftest.py'
#! NOTE: conftest is same as fixture folder in cypress where we keep reusable data

def test_area_fix(my_rectangle):              
    assert my_rectangle.area() == 7 * 3       
    
def test_perimeter_fix(my_rectangle):          
    assert my_rectangle.perimeter() == 7 * 2 + 3 * 2 
    
    