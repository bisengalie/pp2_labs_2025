import math
#1 converge degree to radian
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

#2 calculate area of trapezoid
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

#3 calculate area of polygon
num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", round(area, 6))

#4 calculate area of parallelogram
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area) 
