import re

def snakeToCamel(string):
    camel = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), string)
    return camel

string = input()
print(snakeToCamel(string))
