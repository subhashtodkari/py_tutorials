#!/bin/python3

import math
import os
import random
import re
import sys


def match(a: str, ai: int, b: str, bi: int):
    if bi == len(b):
        while ai < len(a):
            if a[ai].isupper():
                return False
            ai += 1
        return True
    while ai < len(a):
        if a[ai].upper() == b[bi]:
            matched = match(a, ai+1, b, bi+1)
            if matched:
                return True
        elif a[ai].isupper():
            return False
        ai += 1
    return False


# Complete the abbreviation function below.
def abbreviation(a, b):
    matched = match(a, 0, b, 0)
    return "YES" if matched else "NO"


if __name__ == '__main__':
    a = "daABcd"
    b = "ABC"
    print(a, b)
    print(abbreviation(a, b))