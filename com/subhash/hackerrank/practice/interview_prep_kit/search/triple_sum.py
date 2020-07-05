#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    sorted_b = sorted(set(b))
    sorted_a = sorted(set(a))
    sorted_c = sorted(set(c))
    ai = 0
    ci = 0
    bi = 0
    count = 0
    while bi < len(sorted_b):
        bb = sorted_b[bi]
        while ai < len(sorted_a) and sorted_a[ai] <= bb:
            ai += 1
        while ci < len(sorted_c) and sorted_c[ci] <= bb:
            ci += 1
        count += (ai * ci)
        bi += 1
    return count
    


if __name__ == '__main__':

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    print(ans)
