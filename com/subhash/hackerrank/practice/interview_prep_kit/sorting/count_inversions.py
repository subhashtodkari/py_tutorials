#!/bin/python3

import math
import os
import random
import re
import sys


def merge_sort(arr, new_arr, left, right):
    # print("arr, left, right >> ", arr, left, right)
    if right == left:
        # print("returning swaps: 0")
        new_arr[left] = arr[left]
        return 0
    if right - left == 1:
        if arr[right] < arr[left]:
            # print("returning swaps: 1")
            new_arr[left] = arr[right]
            new_arr[right] = arr[left]
            return 1
        else:
            # print("returning swaps: 0")
            new_arr[left] = arr[left]
            new_arr[right] = arr[right]
            return 0

    mid = (right + left) // 2

    swaps_left = merge_sort(arr, new_arr, left, mid-1)
    swaps_right = merge_sort(arr, new_arr, mid, right)

    swaps = swaps_left + swaps_right

    # print("before merge, left: ", arr_left, left, mid-1)
    # print("before merge, right: ", arr_right, mid, right)

    # merge 2 halves if required i.e. first of right half is smaller than last of left

    if new_arr[mid] < new_arr[mid-1]:
        temp_arr_size = right - left + 1
        temp_arr = [0] * temp_arr_size
        t = 0
        l = left
        r = mid

        while l < mid and r <= right:
            if new_arr[l] <= new_arr[r]:
                temp_arr[t] = new_arr[l]
                l += 1
            else:
                # r is swapping (mid-1-left+t)
                temp_arr[t] = new_arr[r]
                swaps += (mid-l)
                r += 1
            t += 1

        # if there are swaps then only perform further copy else original array is good

        # copy left array remaining items
        while l < mid:
            temp_arr[t] = new_arr[l]
            l += 1
            t += 1

        # copy right array remaining items
        while r <= right:
            temp_arr[t] = new_arr[r]
            r += 1
            t += 1

        # copy temp array into new array
        t = 0
        while t < temp_arr_size:
            new_arr[left + t] = temp_arr[t]
            t += 1

    # print("returning swaps: ", swaps)
    return swaps


# Complete the countInversions function below.
def countInversions(arr):
    new_arr = [0] * len(arr)
    swaps = merge_sort(arr, new_arr, 0, len(arr)-1)
    return swaps


if __name__ == '__main__':

        arr = [2, 1, 3, 1, 2]

        # arr = list(map(int, "1 5 3 7".split()))

        result = countInversions(arr)

        print(arr, " ==> ", result)
