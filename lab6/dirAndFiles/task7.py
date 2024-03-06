file = open("text.txt","r")
file2 = open("text2.txt","w")
for i in file:
    file2.write(i)
file.close()
file2.close()



