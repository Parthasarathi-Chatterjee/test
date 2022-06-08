number= int(input("Eenter a number: "))
i=number-1
flag=True
while(i>1):
    if(number % i ==0):
       flag = False
       break
    i-=1
if (flag):
    print("number is prime")
else:
    print("number is not prime")

       

