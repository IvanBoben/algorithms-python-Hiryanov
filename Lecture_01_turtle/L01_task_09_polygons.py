"""
Draws 10 polygons. Every next one has 1 more sides.
Each inside the another with the same center point.
"""

import turtle
import math

# Makes the cursor looks like turtle.
turtle.shape('turtle')

def polygon(sides, radius):
	"""
	Draws a polygon using an amount of sides and the radius of
	the circumscribed circle of the polygon.

	:param sides: an amount of sides
	:param radius: a radius of circumscribed circle
	"""

	# Calculates the main angle for other calculations.
	angle = 360 / sides

	# Calculates the length of the side of the polygon
	# using the tricky formula of circumscribed circle.
	angle_radians = math.radians(angle / 2)
	sinus = math.sin(angle_radians)
	length = 2 * (radius * sinus)

	# Turns to the left before the drawings to take the correct
	# starting position.
	turtle.left((angle / 2) + 90)

	# Initializes a cycle with amount of iterations equals amount of sides.
	for x in range(sides):

		# Draws a line and turn to the left by the value of the main angle.
		turtle.forward(length)
		turtle.left(angle)

	# Turns to the right after the drawings to make the alignment and
	# being ready for next actions.
	turtle.right((angle / 2) + 90)

# Sets an amount of sides of the first polygon.
sides = 3

# Sets a radius of the circumscribed circle of the first polygon
radius = 30

# Sets an indent after drawing a polygon and before starting to draw
# a next polygon. Uses the first radius value to avoid interceptions.
# Indent is fixed and will not be changed.
indent = radius * 0.7

# Initializes a cycle with 10 iterations for each polygon.
for y in range(10):

	# Draws a polygon using an amount of sides and the radius of
	# the circumscribed circle of the polygon.
	polygon(sides, radius)

	# Disables drawing and makes an indent. Then enable drawing again.
	turtle.penup()
	turtle.forward(indent)
	turtle.pendown()

	# Increase the amount of sides for the next polygon by 1.
	sides += 1

	# Increase the radius of the circumscribed circle of
	# the next polygon by fixed indent.
	radius += indent

# Stops the turtle so you can see the result.
turtle.mainloop()