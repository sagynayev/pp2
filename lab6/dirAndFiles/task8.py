import os
exis = input()
if os.path.exists(exis):
    print("Yes")
    os.remove()
else:
    print("no")