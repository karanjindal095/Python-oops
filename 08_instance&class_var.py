class employee:
    comp_name = "Apple"        #class variable
    def __init__(self,name):
        self.name = name       #instance variable
        self.amount = 500 
    def info(self):
        print(f"The name of employee is {self.name} and the amount in {self.comp_name} is {self.amount}")

# employee.info(e)  =  e.info()
e = employee("Karan")
e.amount = 600
e.comp_name = "Apple india"
e.info()

employee.comp_name = "google"
print(employee.comp_name)

e1 = employee("Harry")
e1.info()