class company:
    def person1(s):
        print("hello i am person 1")

class employee(company):
    def person1(s):
        print("Hello")

    def person2(s):
        print("Hello i am person 2")
        super().person1()  # it will call comp p1
        

obj = employee()
obj.person1()  # it will call empl p1
obj.person2()  # it will call both p1 of comp and p2 of empl

class worker:
    def __init__(s,name,id):
        s.name = name
        s.id = id

class programmer(worker):
    def __init__(s,name,id,lang):
        super().__init__(name,id)
        s.lang = lang 

rohan = worker("Rohan",400)
Karan = programmer("KAran",500,"Python")
print(Karan.name)
print(Karan.id)
print(Karan.lang)
