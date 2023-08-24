class person:
    name = "karan"
    occ = "developer"
    def __init__(self,a,b):
        print(f"{self.name} is a {self.occ}")
        sum = a+b
        print(sum)
obj = person(10,20)
obj1 = person(50,60)

class employee:
    def __init__(self,n,o):
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

obj3 = employee("karan ","python developer")
obj3.info()