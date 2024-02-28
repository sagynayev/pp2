import re

string = input()
pattern = '^[a-z]+_[a-z]+'

if re.search(pattern, string):
    print("Match found!")
    result = re.findall(pattern, string)
    print(result)
else:
    print("No match found.")