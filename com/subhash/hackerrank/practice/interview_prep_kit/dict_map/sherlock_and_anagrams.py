#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def sherlockAndAnagrams(s):
    result = 0

    mp = defaultdict(list)

    for i in range(len(s)):

        # find substrings of length i + 1
        for j in range(len(s) - i):
            # print("--> ", s[j:j+i+1])
            w = s[j:j+i+1]
            pos = j

            # sort w
            w = ''.join(sorted(w))
            mp[w].append(pos)

    # print("mp --> ", mp)

    # count occurrences
    for lst in mp.values():
        if len(lst) > 1:
            result += (len(lst) - 1) * (len(lst)) / 2
            # print(lst, result)

    return int(result)


if __name__ == '__main__':
    s = "kkkk"
    result = sherlockAndAnagrams(s)
    print(str(result))


