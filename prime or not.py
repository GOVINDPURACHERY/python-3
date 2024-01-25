num=int(input("enter number:"))
a=num//2
temp=0
for i in range(2,a):
    if (num%i) == 0:
        temp=1
        break
if temp==1:
    print("this is not a prime number")
else:
    print("this is a prime number")
    
