file_Read=open("Data.txt","r")
file_Write=open("Data2.txt","w")
for data in file_Read:
    print(data,file=file_Write)