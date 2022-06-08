sum=0
num= int(input("enter your number: "))

while(num > 0):
    r= num%10
    sum+= r
    num=num/10
print(sum)

