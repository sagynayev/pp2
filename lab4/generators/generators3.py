def divisibled_3_4(a,b):
    for i in range(a,b+1):
        if i % 3 ==0 and i % 4 == 0:
            yield i

a = 0
b = int(input("Write number= "))
divisibleNums = divisibled_3_4(a, b)
for num in divisibleNums:
    print(num)