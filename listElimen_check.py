demoList = [3,5,9,11,23,43,54,1,7]
num = 5
f = False
pos = 0
for i in demoList:
    if(i == num):
        f = True
        break
    pos += 1

if(f):
    print(str(num) + " found at position " + str(pos))
else:
    print("element is not exist")