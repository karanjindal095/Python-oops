# 01 getters
class myclass:
    def __init__(self,v):
        self.value = v
    
    def dis(self):
        print(f"value is {self.value}")

    @property
    def getvalue(self):
        return 10*self.value
    
    @getvalue.setter
    def getvalue(self,newv):
        self.value = newv
        
obj = myclass(10)
obj.dis()
print(obj.getvalue,"\n")

obj1 = myclass(10)
obj1.getvalue = 100
obj1.dis()
print(obj1.getvalue)