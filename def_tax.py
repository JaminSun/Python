def Tax(salary):
    if salary>1500:
        T=salary*20/100
    else:
        T=salary*15/100
    return T
salary=int("Enter you salary:")
print("Your tax:",tax(salary))
print("Net",(salary-tax(salary))