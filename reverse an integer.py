num=int(input("number:"))
reverse_num=0
while (num > 0):
    reminder=num % 10
    reverse_num=(reverse_num*10)+reminder
    num=num // 10
print(reverse_num)
    
# number = int(input("Enter the integer number: "))  
# revs_number = 0  
# while (number > 0):  
#     remainder = number % 10  
#     revs_number = (revs_number * 10) + remainder  
#     number = number // 10  
# print("The reverse number is : {}".format(revs_number))
