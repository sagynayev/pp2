def spy_game(nums):
    code = [0, 0, 7]  # Define the code pattern
    index = 0         # Start with the first digit of the code
    for num in nums:
        if num == code[index]:
            index += 1  # Move to the next digit of the code
            if index == len(code):
                return True  # Found the complete code
    return False

# Test cases
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False
