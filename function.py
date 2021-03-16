def say_hi():
    print("Hello world!!!")

say_hi()

def sum(x,y):
    c = float(x) + float(y)
    return c

x = input("Enter first number: ")
y = input("Enter second number: ")
c = sum(x,y)
print(c)
print("Addition is : "+ str(c))