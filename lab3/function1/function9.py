import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius ** 3
    return volume

radius = 3
print("Объем сферы s радиусом", radius, "ровно: ", sphere_volume(radius))
