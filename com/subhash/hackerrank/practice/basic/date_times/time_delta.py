import math
import os
import random
import re
import sys
from dateutil.parser import parse


# Complete the time_delta function below.
def time_delta(t1, t2):
    dt1 = parse(t1)
    dt2 = parse(t2)
    diff = int((dt1 - dt2).total_seconds())
    if diff < 0:
        diff = -diff
    #print(diff)
    return str(diff)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        # t1 = "Sun 10 May 2015 17:30:00 +0530"
        # t2 = "Sun 10 May 2015 12:05:00 -0000"

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()