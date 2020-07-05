#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    ca = dict()
    for num in arr:
        ca[num] = (0 if num not in ca else ca[num]) + 1

    count = 0
    for num in ca.keys():
        num_c = ca[num]
        num_plus_diff = num + k
        num_plus_diff_c = 0 if num_plus_diff not in ca else ca[num_plus_diff]
        count += num_c * num_plus_diff_c

    return count



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    print(result)
