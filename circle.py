import math

PI = math.pi

def area(radius):

	area_of_circle = PI * (radius * radius)
	
	return f"The area of the circle is: {area_of_circle:.2f}"

print(area(4))