from abc import AB,abstractmethod
class Shape(AB):
    @abstractmethod
    def area(self):
        pass
class rec(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print(f"the area of rec:{self.length*self.breadth}")
class cir(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print(f"the area of circle:",3.14*self.radius*self.radius)
obj=rec(3,4)
obj.area()
obj1=cir(5)
obj1.area()

