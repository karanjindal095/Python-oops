class employee:
    def __init__(self):
        self.name = "karan"         #Public
        self._city = "malerkotla"   #Protected
        self.__post = "developer"   #Private

obj = employee()
print(obj.name)             #Public

print(obj._city)            #Protected

# print(obj.__post)         #error bcoz Private

print(obj._employee__post)  #accessing indirectly ( Name Mangling )
