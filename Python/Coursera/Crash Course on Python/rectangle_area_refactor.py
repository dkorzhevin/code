# Refactor function to calculate the area of a rectangle

# Before refactor:

#def f1(x, y):
#	z = x*y  # the area is base*height
#	print("The area is " + str(z))
	
# After refactor:

def rectangle_area(base, height):
	area = base * height  # the area is base * height
	print("The area is " + str(area))
	
rectangle_area(5, 6)