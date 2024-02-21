def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits

numheads = int(input("heads: 35 "))
numlegs = int(input("legs: 94 "))

chickens, rabbits = solve(numheads, numlegs)

print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)
