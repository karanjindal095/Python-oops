def greet(fx):
    def g(*n):
        print("let's begin")
        fx(*n)
        print("Thanks")
    return g

@greet
def hi():
    print("hello world")

def add(a,b):
    print(a+b)

hi()

print(" ")
add(10,20)
print(" ")

greet(add)(11,9)