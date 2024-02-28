import re

string = input()
print(re.findall('[A-Z][^A-Z]*', string))