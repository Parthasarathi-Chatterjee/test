number= int(input("Eenter a number: "))
flag=True
for i in range(2, number-1):
    if(number % i==0):
        flag= False
        break
if(flag == True):
    print("number is  prime")
else:
    print("number is not prime")

