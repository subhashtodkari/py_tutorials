if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happiness = 0
    for i in lst:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
        else:
            pass
    print(happiness)

