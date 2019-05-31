def addition(a,b):
    c=a+b
    print("Result of addition",c)

def subtraction(a,b):
    c=a-b
    print("Result of subtraction",c)

def operation(F,a,b):
    F(a,b)

operation(addition,20,10)
operation(subtraction,20,10)