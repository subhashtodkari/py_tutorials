from collections import Counter


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if len(note) > len(magazine):
        print("No")
        return

    mgzn_map = Counter(magazine)
    note_map = Counter(note)
    # print(mgzn_map)
    # print(note_map)
    for w in note:
        note_cnt = note_map[w]
        mgzn_cnt = mgzn_map[w]
        if note_cnt > mgzn_cnt:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
