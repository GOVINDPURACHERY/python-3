#low to high
a=[1,4,2,67,44,39,99]
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)

#hight to low
a=[1,4,2,67,44,39,99]
n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]<a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
