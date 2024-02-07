from itertools import permutations

def printPermutations(string):
    perms = permutations(string)
    for x in perms:
        print(''.join(x))
userWrite = input("String: ")
printPermutations(userWrite)
