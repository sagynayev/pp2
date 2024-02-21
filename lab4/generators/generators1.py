def squares_generator(N):
    for i in range(N+1):
        yield i ** 2

N = int(input("N="))
squares = squares_generator(N)
for square in squares:
    print(square)
