import re

string = input()
pattern = '[A-Z]+[a-z]+'

if re.search(pattern, string):
    print("Match found!")
    result = re.findall(pattern, string)
    print(result)
else:
    print("No match found.")