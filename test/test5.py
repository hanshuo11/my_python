#!/user/bin/env python
# Author:HanShuo
# ax2 + bx + c = 0
import math


def quadratic(a, b, c):
    p = b * b - 4 * a * c
    w=2*a
    x1 = (-b + math.sqrt(p)) / w
    x2 = (-b - math.sqrt(p)) / w
    return x1, x2


print(quadratic(2, 3, 1))
