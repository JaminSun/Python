def ones(num):
    result=""
    if num==1:
        result="One"
    if num==2:
        result="Two"
    if num==3:
        result="Three"
    if num==4:
        result="Four"
    if num==5:
        result="Five"
    if num==6:
        result="Six"
    if num==7:
        result="Seven"
    if num==8:
        result="Eight"
    if num==9:
        result="Nine"
    if num==10:
        result="Ten"
    if num==11:
        result="Eleven"
    if num==12:
        result="Twelve"
    if num==13:
        result="Thirteen"
    if num==14:
        result="Fourteen"
    if num==15:
        result="Fifteen"
    if num==16:
        result="Sixteen"
    if num==17:
        result="Seventeen"
    if num==18:
        result="Eighteen"
    if num==19:
        result="Nineteen" 
    return result

def tens(num):
    result=""
    if num==20:
        result="Twenty"
    if num==30:
        result="Thirty"
    if num==40:
        result="Fourty"
    if num==50:
        result="Fifty"
    if num==60:
        result="Sixty"
    if num==70:
        result="Seventy"
    if num==80:
        result="Eighty"
    if num==90:
        result="Ninety"
    return result

num=int(input("Enter a number from 1-9999:"))
ans=""
if num>=1000 and num<=9999:
    ans += ones(int(num/1000))+" Thousand "
    num = num%1000
if num>=100 and num<=999:
    ans += ones(int(num/100))+" Hundred "
    num = num%100
if num>=20 and num<=100:
    ans += tens(int(num%10)*10)+" "
    num = num%10
if num>=0 and num<=19:
    ans += ones(num)
print(ans)

    
    


