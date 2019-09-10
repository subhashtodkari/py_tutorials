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


def how_to_use_sets():
    s = set()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(2)
    print("Set s: ", s)
    arr = [10, 20, 30]
    s.update(arr)
    print("Set after update(arr) s: ", s)


def how_to_use_lists():
    ll = list()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(2)
    print("List ll: ", ll)
    arr = [10, 20, 30]
    # list.append(collection) will add collection as single object
    ll.append(arr)
    print("List after append(arr) ll: ", ll)
    # list.extend(collection) will add individual items to list
    ll.extend(arr)
    print("List after extend(arr) ll: ", ll)
    ll.insert(0, "first")
    print("List after insert(0, ", "First", ") ll: ", ll)


def how_to_use_map_or_dict():
    d = dict()
    d[1] = "one"
    d[2] = "two"
    d[3] = "three"
    # overrides
    d[1] = "ONE"
    print("Dictionary: ", d)
    print("Dictionary check key 5: ", 5 in d)
    print("Dictionary get value of 2: ", d[2])
    print("Dictionary pop last inserted item: ", d.popitem())
    print("Dictionary: after popitem(): ", d)
    print("Dictionary: pop(1): ", d.pop(1))
    print("Dictionary: after pop(1): ", d)
    d.update({10: "ten", 20: "twenty", 30: "thirty"})
    print("Dictionary: after update(another dict): ", d)


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
    how_to_use_sets()
    how_to_use_lists()
    how_to_use_map_or_dict()
