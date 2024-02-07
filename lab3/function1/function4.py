def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    primeNumbers = []
    for n in numbers:
        if is_prime(n):
            primeNumbers.append(n)
    return primeNumbers

numbers = input("Write numbers: ").split()
numbers = [int(n) for n in numbers]
primeNumbers = filter_prime(numbers)
print("Prime Numbers: ", primeNumbers)
