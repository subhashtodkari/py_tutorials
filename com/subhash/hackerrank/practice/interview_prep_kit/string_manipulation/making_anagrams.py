#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    del_count = 0
    for (char_a, cnt_a) in counter_a.items():
        if char_a in counter_b:
            cnt_b = counter_b[char_a]
            del_count += abs(cnt_b - cnt_a)
            counter_b.pop(char_a)
        else:
            del_count += cnt_a

    for cnt_b in counter_b.values():
        del_count += cnt_b

    return del_count


if __name__ == '__main__':
    a = "abc"
    b = ""
    res = makeAnagram(a, b)
    print(res)
