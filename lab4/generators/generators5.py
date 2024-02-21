def countdown(N):
    while N>=0:
        yield N
        N-=1

N = int(input("Write number="))
countDownGenerator = countdown(N)
for num in countDownGenerator:
    print(num)
