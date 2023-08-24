class person:
    name = "karan jindal"
    post = "software developer"
    course = "bca"
    def about(self):
        print(f"\n{self.name} is a {self.post} with a degree of {self.course}\n")

    def arith(a,b,c):
        a = int(input("enter the no. : "))
        sq = a**(0.5)
        print(sq)
        sum = b + c
        print(sum)

obj = person()
obj1 = person()
obj1.name = "ram singla"
obj1.post = "data scintist"
obj1.course = "mca"
obj.about()
obj1.about()
obj.arith(10,20)
