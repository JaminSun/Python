msg = input("Enter any message:")
word=""
i=0
c=0
while c<len(msg):
    if ord(msg[c])>=65 and ord(msg[c])<=90:
        word += chr(ord(msg[c])+32)
    else:
        if ord(msg[c])>=97 and ord(msg[c])<=122:
            word += chr(ord(msg[c])-32)
        else:
            if ord(msg[c])>=48 and ord(msg[c])<=57:
                word += chr(ord(msg[c]))*2
            else:
                print("Any other character")
    c += 1  
print(word)