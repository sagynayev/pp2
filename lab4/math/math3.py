import math

numSides = int(input("Input number of sides: "))

sideLength = float(input("Input the length of a side: "))

area = (numSides * sideLength ** 2)/(4 * math.tan(math.pi / numSides))

print("The area of the polygon is: ", area)
