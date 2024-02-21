def evenNumbers(N):
    for i in range(N+1):
        if i%2==0:
            yield i

N = int(input("Write N="))
evenNums = evenNumbers(N)
print(", ".join(str(num) for num in evenNums))