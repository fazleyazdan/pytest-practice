import pytest
import source.shapes as shapes

def test_square():
    assert shapes.Square(5).area() == 25
    


#! suppose you wanna test 'Square' for multiple values, then we have to use parameterization
#* here below we have used list of tuples. first we have to specify the parameters and then pass their values.
#* it is beneficial because we are not using loop and testing multiple values and their results

@pytest.mark.parametrize("side_length, expected_area", [(4, 16), (5, 25) ,(7,49)])
def test_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area
    
    
#! for Perimeter
@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5,20)])
def test_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter