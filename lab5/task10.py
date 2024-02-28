import re

string = input()
temp = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', temp).lower())