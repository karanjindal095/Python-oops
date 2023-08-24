class employee:
    company = "Apple"
    def show(s):
        print(f"The name is {s.name} and company is {s.company}")

    @classmethod                # using class decorater
    def changecomp(s,newname):  # bcoz using ^ method first argument will be class rather than object
        s.company = newname

e = employee()
e.name = ("Karan")
e.show()
e.changecomp("Google")
e.show()
print(employee.company)
