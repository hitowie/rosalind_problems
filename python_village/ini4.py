#!/usr/bin/env python3

import sys

def sum_odds(a, b):
    odd_sum = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            odd_sum += i
    return odd_sum

print(sum_odds(int(sys.argv[1]), int(sys.argv[2])))