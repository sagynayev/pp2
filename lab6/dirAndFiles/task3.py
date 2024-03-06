import os
text=input("Write the path to dir:") #/Alimzhan/pp2
if os.path.exists(text):
    print("Exists: True")
    print("Directory:",os.path.basename(text))
    print("Filename:",os.path.dirname(text))
else:
    print("It doesn't exist")
