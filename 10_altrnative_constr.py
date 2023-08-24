# class method as alternative constructors
class employee:
    def __init__(s,name,salary):
        s.name = name
        s.salary = salary
    @classmethod
    def fromstr(s,string1):
        return s(string1.split("-")[0],int(string1.split("-")[1]))

e = employee("Karan",15000)
print(e.name)
print(e.salary)

string = "Rahul-12000"
e1 = employee(string.split("-")[0],int(string.split("-")[1]))
print(e1.name)
print(e1.salary)

string1 = "Rohan-10000"
e2 = employee.fromstr(string1)
print(e2.name)
print(e2.salary)
print(f"Total salary {int(e.salary+e1.salary+e2.salary)}")