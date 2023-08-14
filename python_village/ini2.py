#!/usr/bin/env python3

import sys
import math

def pythagoras(a, b):
    c_square = a ** 2 + b ** 2
    return c_square

print(pythagoras(int(sys.argv[1]), int(sys.argv[2])))