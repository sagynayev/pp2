import re

with open('C:/Alimzhan/pp2/lab5/row/row.txt', 'r', encoding='utf-8') as f:
    text = f.read()
patternBody = r'Фискальный признак:(.*)WEBKASSA.KZ'
matchingBody = re.search(patternBody, text, re.DOTALL)
if matchingBody is not None:
    print(matchingBody.group())