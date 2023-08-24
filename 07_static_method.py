class math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a+b
    
obj = math(5)
print(obj.num)
obj.addtonum(6)
print(obj.num)

print(obj.add(9,1))
print(math.add(9,1))

    