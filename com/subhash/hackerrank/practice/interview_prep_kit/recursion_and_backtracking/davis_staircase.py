#!/bin/python3

import math
import os
import random
import re
import sys


ways_to_climb = 0
modulo_by = 10000000007
steps = [1, 2, 3]

# memoization
cache = dict()

# Complete the stepPerms function below.
def stepPerms(n):
    global ways_to_climb

    if n in cache:
        ways_to_climb += cache[n]
        return cache[n]

    for step in steps:
        n -= step
        if n == 0:
            ways_to_climb += 1
        elif n > 0:
            stepPerms(n)
        n += step

    cache[n] = ways_to_climb % modulo_by
    return cache[n]


if __name__ == '__main__':
    ns = [5, 1, 3, 7]
    for n in ns:
        ways_to_climb = 0
        res = stepPerms(n)
        print(res)
