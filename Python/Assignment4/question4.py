class Shape:
  def area(self):
   print("Areas")

class Circle(Shape):
  def area(self,r):
    pi=3.14
    area=pi*(r*r)
    return area

class Rectangle(Shape):
  def area(self,l,b):
    area=l*b
    return area

class Triangle(Shape):
  def area(self,b,h):
    area=1/2*(b)*(h)
    return area

cal=Shape()
cir=Circle()
rect=Rectangle()
tri=Triangle()

cal.area()
print(f"Area of Circle is {cir.area(8)}")
print(f"Area of Rectangle is: {rect.area(6,5)}")
print(f"Area of Triangle is: {tri.area(8,12)}")