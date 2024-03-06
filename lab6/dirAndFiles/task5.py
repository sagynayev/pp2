def writeListToFile(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filename = "pp2/lab6/dirAndFiles/listData.txt"
writeListToFile(filename, data)
