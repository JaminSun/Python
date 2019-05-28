msg = input("enter message:")
word = 0
i = 0
while i<len(msg):
    if msg[i]==" ":
        word=word+1
    i=i+1
if word+1==1:   
    print("There is",(word+1),"word")
else:
    print("There are",(word+1),"words")