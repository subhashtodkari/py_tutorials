#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    left_2_right_arr = [1] * len(arr)
    right_2_left_arr = [1] * len(arr)
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            left_2_right_arr[i] = left_2_right_arr[i - 1] + 1
        if arr[-i-1] > arr[-i]:
            right_2_left_arr[-i-1] = right_2_left_arr[-i] + 1
        # print(left_2_right_arr)
        # print(right_2_left_arr)
        # print()
    min_candies = 0
    for i in range(len(arr)):
        min_candies += max(left_2_right_arr[i], right_2_left_arr[i])

    return min_candies


if __name__ == '__main__':
    n = 10
    arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]

    print("n: ", n)
    print("arr: ", arr)

    min_candies = candies(n, arr)
    print("min_candies: ", min_candies)