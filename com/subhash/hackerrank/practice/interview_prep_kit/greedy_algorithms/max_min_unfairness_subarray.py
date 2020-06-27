#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    min_diff = arr[k - 1] - arr[0]
    for i in range(k, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - k + 1])
        if min_diff == 0:
            return 0
    return min_diff


if __name__ == '__main__':
    '''
    5
    2
    1
    2
    3
    3
    4
    '''
    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result))
