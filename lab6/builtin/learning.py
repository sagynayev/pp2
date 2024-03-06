#
nums = [1, 2, 3, 4, 5]

nums_doubled = map(lambda x : x * 2, nums)

print(nums_doubled)
#
nums = [1, 2, 3, 4, 5]

map_obj = map(str, nums)

print(next(map_obj))

print(', '.join(map(str, nums)))
#
nums = [1, 2, 3, 4, 5]

reversed_nums = list(reversed(nums))

print(reversed_nums)
#
word = "banana"

reversed_word = ''.join(reversed(word))

print(reversed_word)
#
nums = list(range(1, 51))

nums_even = list(filter(lambda x : x % 2 == 0, nums))

print(nums_even)
#


from math import sqrt

nums = list(range(1, 51))

def is_prime(x):
    if(x == 1):
        return False
    root = round(sqrt(x))
    for i in range(2, root + 1):
        if x % i == 0:
            return False
    return True

nums_prime = list(filter(is_prime, nums))

print(nums_prime)
#
nums = [3, -4, 7, 11, 2]

print(sum(nums))
print(max(nums))
print(min(nums))

#
A_ascii = 65

print(chr(A_ascii))

A_symbol = 'A'

print(ord(A_symbol))

#

from math import sqrt

nums = list(range(1, 51))

def is_prime(x):
    if(x == 1):
        return False
    root = round(sqrt(x))
    for i in range(2, root + 1):
        if x % i == 0:
            return False
    return True

nums_isprime = list(map(is_prime, nums))

print(nums_isprime)

amount_of_primes = sum(nums_isprime)

print(amount_of_primes)
#
