find=input("What are you looking for:")
replace=input("Replace with what:")
f_read=open("Data.txt","r")
f_write=open("Data2.txt","w")
for Data in f_read:
    i=0
    while i<len(Data):
        if Data[i]==find[0]:
            if Data[i:len(find)+i]==find:
                print(replace,end="",file=f_write)
                i+=len(find)-1
            else:
                print(Data[i],end="",file=f_write)
        else:
            print(Data[i],end="",file=f_write)
            i+=1