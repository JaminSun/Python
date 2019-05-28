msg=input("Enter your message:")
find=input("What word are you looking for?:")
f=0
i=0
while i<len(msg):
    if msg[i]==find[0]:
        if msg[i:i+len(find)]==find:
            f=f+1
            i=i+len(find)-1
    i=i+1
print(f)