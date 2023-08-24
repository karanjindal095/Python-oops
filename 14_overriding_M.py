class shape:
    def __init__(s,x,y):
        s.x = x
        s.y = y
        # s.x = int(input("enter the no. "))
        # s.y = int(input("enter the no. "))

    def area(s):
        return s.x * s.y
    
class circle(shape):
    def __init__(s,radius):
        s.r = radius
        super().__init__(radius,radius)
    def area(s):
        # return 3.14 * s.r* s.r
        return 3.14 * super().area()

rec = shape(5,5)
print(rec.area())
c = circle(10)
print(c.area())