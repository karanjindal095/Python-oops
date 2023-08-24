# 01 dir()
# x = [1,2,3]
# print(dir(x))
# print(x.__add__)

# 02 dict() or__dict__
class person:
    def __init__(s,name,age):
        s.name = name
        s.age = age
        s.rollno = 2213828

p = person("Karan",19)
print(p.__dict__) 

# 03 help()
# print(help(p.__dict__))