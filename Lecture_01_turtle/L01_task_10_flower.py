"""
Draws a flower by 6 circles.
In fact, the circles is just a high quality polygons.
"""

import turtle

# Makes the cursor looks like turtle.
turtle.shape('turtle')

def circle_left(length, angle):
	"""
	Draws a circle to the left. In fact, the circle is just
	a high quality polygon.

	:param length: a length of a side of a polygon
	:param angle: an angle of a turn between sides
	"""

	# Turns to the left by a half of the angle.
	# Taking the starting positon.
	turtle.left(angle / 2)

	# Draws a circle to the left using the amount of sides,
	# the length of the sides and the angle between them.
	for i in range(sides):
		turtle.forward(length)
		turtle.left(angle)

	# Turns to the left by a half of the angle.
	# Making the alignment after the drawings.
	turtle.left(angle / 2)


def circle_right(length, angle):
	"""
	Draws a circle to the right. In fact, the circle is just
	a high quality polygon.

	:param length: a length of a side of a polygon
	:param angle: an angle of a turn between sides
	"""

	# Turns to the right by a half of the angle
	# Taking the starting positon.
	turtle.right(angle / 2)

	# Draws a circle to the right using the amount of sides,
	# the length of the sides and the angle between them.
	for i in range(sides):
		turtle.right(angle)
		turtle.forward(length)

	# Turns to the right by a half of the angle.
	# Making the alignment after the drawings.
	turtle.right(angle / 2)

# Sets an amount of sides of the polygon. The more sides -
# the more accurate a circle will be.
sides = 45

# Sets a length of a side of a polygon. The more sides -
# the less a length should be.
length = 7

# Sets the angle of a turn between sides.
angle = 360 / sides

# Initializes a cycle with 3 iterations.
for i in range(3):

	# Draws two circles opposite to each other.
	circle_left(length, angle)
	circle_right(length, angle)

	# Turns to the left by 60 degrees.
	turtle.left(60)

# Stops the turtle so you can see the result.
turtle.mainloop()