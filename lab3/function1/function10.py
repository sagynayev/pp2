def unique_elements(inputList):
    uniqueList = []
    for x in inputList:
        if x not in uniqueList:
            uniqueList.append(x)
    return uniqueList

firstList = [1, 2, 3, 3, 4, 4, 5]
print("Первоначальный список:", firstList)
print("Лист s уникальными элементами:", unique_elements(firstList))
