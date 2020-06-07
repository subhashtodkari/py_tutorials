#!/bin/python3

import math
import os
import random
import re
import sys

# memoization
r1 = dict()


def match(a: str, ai: int, b: str, bi: int):
    if bi == len(b):
        if ai in r1:
            return r1[ai]
        while ai < len(a):
            if a[ai].isupper():
                r1[ai] = False
                return False
            ai += 1
        r1[ai] = True
        return True
    while ai < len(a):
        if a[ai].upper() == b[bi]:
            matched = match(a, ai+1, b, bi+1)
            if matched:
                return True
        elif a[ai].isupper():
            return False
        ai += 1
    return False


def match_dp(a: str, b: str):
    dp = [[False for x in range(len(b)+1)] for y in range(len(a)+1)]
    '''
    for r in dp:
        print(r)
    print()
    '''

    # a = "", b = ""
    dp[0][0] = True

    # initial lowercase letter match all as they can be deleted
    for row in range(1, len(dp)):
        if a[row-1].islower():
            dp[row][0] = True
        else:
            break
    '''
    for row in range(len(dp)):
        print(dp[row])
    '''

    for row in range(1, len(dp)):
        for col in range(1, len(dp[row])):
            # print()
            # print("matching row: {}, col: {}, ai: {}, bi {}".format(row, col, a[row-1], b[col-1]))
            # exact match
            if a[row-1] == b[col-1]:
                # print("1 ==> ", dp[row-1][col-1])
                dp[row][col] = dp[row-1][col-1]
            # lowercase matched
            elif a[row-1].upper() == b[col-1]:
                # print("2 ==> ", dp[row-1][col-1], " or ", dp[row-1][col])
                dp[row][col] = dp[row-1][col-1] or dp[row-1][col]
            # failure
            elif a[row-1].isupper():
                # print("3 ==> ", False)
                dp[row][col] = False    # not required, already initialized
            # unmatched lowercase
            else:
                # print("4 ==> ", dp[row-1][col])
                dp[row][col] = dp[row-1][col]

            '''
            print()
            for r in range(len(dp)):
                print(dp[r])
            input()
            '''

    return dp[-1][-1]


# Complete the abbreviation function below.
def abbreviation(a, b):
    matched = match_dp(a, b)
    # matched = match(a, 0, b, 0)
    return "YES" if matched else "NO"


if __name__ == '__main__':
    a = "dacd"
    b = "ABC"
    print(a, b)
    print(abbreviation(a, b))