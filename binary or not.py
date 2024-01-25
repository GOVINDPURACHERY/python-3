num=int(input("enter the number:"))
temp=0
while (num>0):
    reminder=num%10
    if reminder==0 or reminder == 1:
        temp=0
        num=num//10
    else:
        temp=1
        break
if temp==1:
    print("not binary")
else:
    print("binary")

