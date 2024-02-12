import math
from fractions import Fraction
x=60
tangent_degrees= math.tan(math.radians(x))
print('tangent of 45 degrees is', round(tangent_degrees,2), 'or', Fraction(tangent_degrees).limit_denominator())