import re

string = input()
print(re.sub("[ ,.]", ":", string))
