if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m1, m2 = arr[0], arr[1]

    i = 2
    while m1 == m2:
        m2 = arr[i]
        i += 1

    if m2 > m1:
        m1, m2 = m2, m1

    for num in arr[i:]:
        # print("m1: {}, m2: {}, num: {}".format(m1, m2, num))
        if num > m2:
            if num == m1:
                continue
            elif num > m1:
                m1, m2 = num, m1
            else:
                m2 = num

    print(None if m2 >= m1 else m2)

