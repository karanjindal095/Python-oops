class child:
    def __init__(self,name,surname):
        self.n = name
        self.sn = surname
    def myname(self):
        print(f"My name is {self.n} {self.sn}")

class parent(child):
    def add(self):
        self.sum = self.n + self.sn
    
class parent2(parent):
    def dis(self):
        print(self.sum)

obj = parent2("karan","jindal")
obj.myname()
obj.add()
obj.dis()