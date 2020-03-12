import collections


def count_occurrences(lst):

    od = collections.OrderedDict()

    for wrd in lst:
        od[wrd] = od.get(wrd, 0) + 1

    print(len(od))
    print(" ".join("{}".format(v) for v in od.values()))


if __name__ == "__main__":
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(input())
    count_occurrences(lst)

