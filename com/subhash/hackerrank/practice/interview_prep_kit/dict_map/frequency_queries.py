#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    d = dict()
    d2 = dict()
    ans = list()
    for q in queries:
        if q[0] == 1:
            d[q[1]] = 1 if q[1] not in d else d[q[1]] + 1
            d2[d[q[1]]] = 1 if d[q[1]] not in d2 else d2[d[q[1]]] + 1
            if d[q[1]] - 1 in d2:
                d2[d[q[1]] - 1] -= 1
                if d2[d[q[1]] - 1] == 0:
                    del (d2[d[q[1]] - 1])
        elif q[0] == 2:
            if q[1] in d:
                d[q[1]] -= 1
                d2[d[q[1]] + 1] -= 1
                if d2[d[q[1]] + 1] == 0:
                    del (d2[d[q[1]] + 1])

                if d[q[1]] == 0:
                    del (d[q[1]])
                else:
                    d2[d[q[1]]] = 1 if d[q[1]] not in d2 else d2[d[q[1]]] + 1
        else:
            ans.append("1" if q[1] in d2 else "0")
        # print(d, d2)
    return "".join(ans)


if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)