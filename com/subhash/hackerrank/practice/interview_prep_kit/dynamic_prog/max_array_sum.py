#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_sum = 0
    last_2_max_sums = [0] * 2
    for i in range(len(arr)):
        val = arr[i]
        if i == 0:
            max_sum = val
            last_2_max_sums[0] = val
        elif i == 1:
            max_sum = val if val > max_sum else max_sum
            last_2_max_sums[1] = max_sum
        else:
            max_sum = max(val, max_sum, val + last_2_max_sums[0])
            last_2_max_sums = [last_2_max_sums[1], max_sum]
    return max_sum


if __name__ == '__main__':
    arr = [3, 7, 4, 6, 5]
    arr = [-2, 1, 3, -4, 5]
    print(arr)
    print(maxSubsetSum(arr))

