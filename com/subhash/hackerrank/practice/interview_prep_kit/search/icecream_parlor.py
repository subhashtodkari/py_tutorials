#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    d = dict()
    for i in range(len(cost)):
        c = cost[i]
        cc = money - c
        if cc in d.keys():
            print(d[cc] + 1, i + 1)
            return
        d[c] = i
    return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
