import re

string = input()
pattern = r"a(b*)"

if re.match(pattern, string):
    print("Match found!")
    result = re.findall(pattern, string)
    print(result)
else:
    print("No match found.")