ones=["","one","two","three","four","five","six","seven","eight","nine",
"ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["twenty","thirty","fourty","fifty","sixty","seventy","eigthy","ninety"]
num=int(input("Enter any number:"))
ans=""
if num>=1000 and num<=9999:
    ans+=ones[int(num/1000)]+" thousand"
    num=num%1000
if num>=100 and num<=999:
    ans+=ones[int(num/100)]+" hundred"
    num=num%100
if num>=20 and num<=99:
    ans+=tens(int(num/10))
    num=num%10
if num>0 and num<=19:
    ans+=ones(num)
print(ans)