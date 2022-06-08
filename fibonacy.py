number= int(input("Eenter a number: "))
n1=0
n2=1

for i in range(0, number):
    sum = n1 + n2
    n1 = n2
    n2 = sum
    print(sum, end=", ")

