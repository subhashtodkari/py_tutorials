#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the superDigit function below.
# recursive but fails for 3 testcases - might be stack overflow - python limit of 995 stacks
def superDigit(n, k=1):
    sum = int(n[0:1])
    if len(n) > 1:
        sum += superDigit(n[1:])
    sum *= k
    if sum > 9:
        sum %= 9
        sum = 9 if sum == 0 else sum
    return sum

# non recursive
def superDigit_non_recursive(n, k=1):
    sd = int(n) * k % 9
    return sd if sd else 9


if __name__ == '__main__':

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    print(result)