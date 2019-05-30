def reverse(word):
    NewWord=""
    i=len(word)-1
    while i>=0:
        NewWord=NewWord+word[i]
        i-=1
    return NewWord

msg=input("Enter any message:")
NewMsg=""
word=""
for ch in msg:
    if ch==" ":
        NewMsg+=(reverse(word)+" ")
        word=""
    else:
        word+=ch
NewMsg+=(reverse(word)+" ")        
print(NewMsg)