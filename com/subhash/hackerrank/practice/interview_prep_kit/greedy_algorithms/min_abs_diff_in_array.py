#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
from typing import List


def minimumAbsoluteDifference(arr: List):
    n = len(arr)
    arr.sort()
    min_abs_diff = abs(arr[0] - arr[1])
    i = 1
    while i < n - 1:
        min_abs_diff = min(min_abs_diff, abs(arr[i] - arr[i + 1]))
        if min_abs_diff == 0:
            return 0
        i += 1
    return min_abs_diff


if __name__ == '__main__':
    arr = [2, -2, 4]
    result = minimumAbsoluteDifference(arr)
    print(result)
