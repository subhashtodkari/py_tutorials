from collections import Counter


def is_sherlock_valid_string_1(s: str):
    char_counter = Counter(s)
    cnt_counter = Counter(char_counter.values())
    if len(cnt_counter) > 2:
        return "NO"
    if len(cnt_counter) == 2:
        del_cnt = None
        other_cnt = None
        for (cnt, cnter) in cnt_counter.items():
            if cnter == 1:
                del_cnt = cnt
            else:
                other_cnt = cnt
        if not del_cnt or (del_cnt != 1 and del_cnt - other_cnt != 1):
            return "NO"
    return "YES"


def is_sherlock_valid_string(s: str):

    arr = [0] * 26
    for c in s:
        arr[ord(c)-97] += 1
    print(arr)

    cnt_counter = {}
    for i in range(26):
        if arr[i] == 0:
            continue
        cnt_counter[arr[i]] = 1 if arr[i] not in cnt_counter else cnt_counter[arr[i]] + 1

    if len(cnt_counter) > 2:
        return "NO"
    if len(cnt_counter) == 2:
        del_cnt = None
        other_cnt = None
        for (cnt, cnter) in cnt_counter.items():
            if cnter == 1:
                del_cnt = cnt
            else:
                other_cnt = cnt
        if not del_cnt or (del_cnt != 1 and del_cnt - other_cnt != 1):
            return "NO"
    return "YES"


if __name__ == "__main__":
    s = input()
    res = is_sherlock_valid_string(s)
    print(res)
