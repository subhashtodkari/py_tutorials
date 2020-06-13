

def make_alternating(s: str):
    del_count = 0
    prev_char = s[0]
    for i in range(1, len(s)):
        if s[i] == prev_char:
            del_count += 1
        prev_char = s[i]
    return del_count


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input()
        res = make_alternating(s)
        print(res)
