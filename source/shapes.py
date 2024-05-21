class Shapes():
    
   def area(self):
       pass
   
   def perimeter(self):
       pass
        

class Rectangle(Shapes):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
    
    
class Square(Rectangle):
    
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    
    #! you can also do it like this, without inheriting from shapes
    # def __init__(self, side_length, expected_length):   
    #     self.side_length = side_length
    #     self.expected_length = expected_length
        