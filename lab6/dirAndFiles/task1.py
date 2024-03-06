import os

text=input("Write the path of dir:") #/Alimzhan
folders=os.listdir(text)
for i in folders:
    print(i,end=" ")