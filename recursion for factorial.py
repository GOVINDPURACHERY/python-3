num=int(input("enter the number:"))
def recur(a):
    if a==1:
        return 1
    else:
        return a*recur(a-1)
        
print(recur(num))


#looping a function inside the same function
#or a function call inside the same function for looping
