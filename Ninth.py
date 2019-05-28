Spend=int(input("Enter customer spend amount: "))
Owed=int(input("Enter amount owed: "))
Change=Spend-Owed
n50=Change/50
n20=Change%50
n10=Change%20
n5=Change%10
n2=Change%5
n1=Change%2
if n50>0:
    print("50:",int(Change/50))
if n20>0:
    print("20:",int(n50/20))
if n10>0:
    print("10:",int(n20/10))
if n5>0:
    print("5:",int(n10/5))
if n2>0:
    print("2:",int(n5/2))
if n1>0:
    print("1:",int(n5/1))