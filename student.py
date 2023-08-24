# class info:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.age , self.name)

#     def information(self,a,b):
#         print(self.name)
#         print(a+b)

# obj = info("karan",19)
# obj.information(100,400)


# obj2 = info("vanshika",19)
# obj2.information(900,100)

a = input("Enter a no. : ")
print("table of" ,a," is :")
try:
    for i in range(1,11):
        print(int(a),"*" , i,"=" , int(a)*i)
except Exception as e:             #e = tells error
    print(e)                    

print("some imp lines of code")
print("end of program")