# Numeric expressions
2017
2000 + 17
1 + 2 * ((3 * 4 * 5 // 6) ** 3) + 7 + 8 - 9 + 10

# Call expressions
max(3, 4.5)
pow(100, 2)
pow(2, 100)
max(1, -2, 3, -4)
max(min(1, 2), min(3, 4))
# ___(_________, _________)
min(1, 2)
max(1, 3)

# Imports
from operator import add, mul
add(2, 3)
mul(2, 3)
add(1, mul(9, mul(add(4, mul(4, 6)), add(3, 5))))
from math import pi
pi * 71 / 223
from math import sin
sin(pi/2)

# Assignment
radius = 10
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius
radius = 20

# Function values
max
max(3, 4)
f = max
f
f(3, 4)
max = 7
f(3, 4)
f(3, max)
f = 2
# f(3, 4)
__builtins__.max

# User-defined functions
def square(x):
    return mul(x, x)

square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# this = that
def this():
    return that
# this()
that = 100
this()

# Name conflicts
def square(square):
    return mul(square, square)
square(4)
