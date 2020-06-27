#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    return sum([c[i] * ((i // k) + 1) for i in range(len(c))])
    '''
    cost = 0
    for i in range(len(c)):
        m = (i // k) + 1
        cost += c[i] * m
    return cost
    '''


if __name__ == '__main__':
    '''
5 3
1 3 5 7 9
    '''

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(minimumCost)
