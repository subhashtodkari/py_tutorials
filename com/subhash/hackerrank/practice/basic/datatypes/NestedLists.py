if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        lst.append([name, score])

    # print(lst)

    min1 = lst[0][1]
    # print(min1)

    i = 1
    # print("{} == {} = {}".format(min1, lst[i][1], min1 == lst[i][1]))
    while min1 == lst[i][1]:
        i += 1
        # print("i ==> {}".format(i))

    min2 = lst[i][1]
    # print(min2)

    if min2 < min1:
        min1, min2 = min2, min1

    # print("{}, {}".format(min1, min2))

    for itm in lst[i:]:
        if min2 > itm[1]:
            if min1 == itm[1]:
                continue
            elif min1 > itm[1]:
                min1, min2 = itm[1], min1
            else:
                min2 = itm[1]

    # print(min2)

    names = [n[0] for n in lst if n[1] == min2]

    # print(names)

    names.sort()

    for name in names:
        print(name)







