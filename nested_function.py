def operations(day):
    if day==1:
        def fun(A,B):
            C=A+B
            return C
    else:
        def fun(A,B):
            C=A-B
            return C
    return fun

command=operations(int(input("Enter 1 or 2:")))
Num1=int(input("Enter first number:"))
Num2=int(input("Enter second number:"))

print("The result is:",command(Num1,Num2))