try:
    No1=int(input("Enter 1st number:"))
    No2=int(input("Enter 2nd number:"))
    Result=No1/No2
except ValueError:
    print("Please enter digit")