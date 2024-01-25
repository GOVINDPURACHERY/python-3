'''year=int(input("year:"))
result=year%4
if result==0:
    if (year%100)==0:
        if (year%400)==0:
            print("it is a leap year")
        else:
        print("not")
else:
    print("not")'''

year = int(input(""))
if year%100 == 0 and year%400 == 0: 
    print("Leap year")
elif year%100 != 0 and year%4 == 0:
    print("Leap year")
else:
    print("not leap year")



