alpha = input("Enter any character:")
if ord(alpha)>=65 and ord(alpha)<=90:
    print("Upper Case")
else:
    if ord(alpha)>=97 and ord(alpha)<=122:
        print("Lower Case")
    else:
        if ord(alpha)>=48 and ord(alpha)<=57:
            print("Numerical")
        else:
            print("Any other character")