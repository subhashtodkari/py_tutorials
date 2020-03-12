def merge_the_tools(string, k):
    # your code goes here
    t = []
    for i in range(len(string)//k):
        start = i * k
        t.append(string[start: start + k])

    #print(t)

    for s in t:
        u = ""
        for c in s:
            if c not in u:
                u += c
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)