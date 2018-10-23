v=3.14
class Ellipse(object):
    def __init__(self,longsemiaxis,shortsemiaxis):
        self.longsemiaxis=longsemiaxis
        self.shortsemiaxis=shortsemiaxis

    def area(self):
        return self.longsemiaxis*self.shortsemiaxis*v
    
class Circle(Ellipse):
    def __init__(self,semiaxis):
        self.longsemiaxis=semiaxis
        self.shortsemiaxis=semiaxis

class Rectangle(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
class Square(Rectangle):
    def __init__(self,width):
        self.width=width
        self.height=width
        
def compute_area(shapes):
      
      return sum([x.area() for x in shapes])


shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]
total_area=compute_area(shapes)
print(total_area)
