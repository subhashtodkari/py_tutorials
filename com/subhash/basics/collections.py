# various collections (containers)

"""
list
set
dict
tuple
namedtuple
deque
Counter
OrderedDict
defaultdict
"""

from collections import Counter
import re


def how_to_use_array():
    arr = [1, 2, 3, 4, 5]
    print(arr)
    print(arr[3])
    for i in range(1, 3):
        print(arr[i])


def how_to_use_counters():
    cnt = Counter()

    for word in ['first', 'second', "third", "first", "first", 'hi', 'hi', 'hi']:
        cnt[word] += 1

    print(cnt)
    print(cnt['first'])
    print('most common 3 word')
    print(cnt.most_common(3))

    some_big_text = 'In the last lesson, you saw how you could start to make your loop more Pythonic by not keeping track of the loop index manually, but your loop can still be refactored to be more Pythonic.\
                    \
                    In this lesson, you’ll learn that for loops in Python are like “for each” loops in other languages. You can use them to iterate over items from a container or sequence directly and don’t have to look up each item by index.'
    words = re.findall(r'\w+', some_big_text)
    cnt = Counter(words)
    print(cnt.most_common(3))


if __name__ == "__main__":
    print("Demo of Collections/containers used in python");
    how_to_use_array()
    how_to_use_counters()
