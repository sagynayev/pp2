def countCaseLetter(string):
    upperCount = 0
    lowerCount = 0
    for char in string:
        if char.isupper():
            upperCount += 1
        elif char.islower():
            lowerCount += 1
    return upperCount, lowerCount

input = "Astana - Almaty"
upper, lower = countCaseLetter(input)
print("Number of upper case letters:", upper)
print("Number of lower case letters:", lower)
