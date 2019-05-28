msg=input("Enter any message:")
l=input("What are you looking for:")
i=0
c=0
while i<len(msg):
    if msg[i]==l:
        c=c+1
    i=i+1
print (c)