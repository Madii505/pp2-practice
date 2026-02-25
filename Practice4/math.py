import math

# Degree to radian
degree = 15
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

# Area of trapezoid
height = 5
base1 = 5
base2 = 6
area_trap = (base1 + base2) / 2 * height
print("Trapezoid area:", area_trap)

# Area of regular polygon
n = 4
side = 25
area_polygon = (n * side ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", int(area_polygon))

# Area of parallelogram
base = 5
height = 6
area_para = base * height
print("Parallelogram area:", float(area_para))