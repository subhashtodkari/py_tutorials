#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    counting_arr = [0] * 10 ** 4
    non_imp_sum = 0
    imp_contests = 0
    for c in contests:
        if c[1]:
            counting_arr[c[0]] += 1
            imp_contests += 1
        else:
            non_imp_sum += c[0]

    print(imp_contests)
    print(non_imp_sum)
    print(counting_arr)

    i = 0
    k_sum = 0
    non_k_sum = 0
    for j in range(1, len(counting_arr)):
        if counting_arr[j] > 0:
            need_to_win = imp_contests - k - i
            if need_to_win > 0:
                current_win_count = counting_arr[j] if counting_arr[j] <= need_to_win else need_to_win
                k_sum += j * current_win_count
                non_k_sum += j * max(0, (counting_arr[j] - need_to_win))
                i += current_win_count
            else:
                non_k_sum += j * counting_arr[j]

    return non_imp_sum + non_k_sum - k_sum


if __name__ == '__main__':
    '''
8 2
13 1
10 1
9 1
8 1
13 1
12 1
18 1
13 1
    '''
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)

