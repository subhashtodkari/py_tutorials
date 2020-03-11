if __name__ == '__main__':
    s = input()
    alNum = False
    al = False
    num = False
    upper = False
    lower = False

    for i in range(len(s)):
        if alNum and al and num and upper and lower:
            break
        al = True if al else s[i].isalpha()
        num = True if num else s[i].isdigit()
        alNum = True if alNum else al or num
        lower = True if lower else s[i].islower()
        upper = True if upper else s[i].isupper()

    print(alNum)
    print(al)
    print(num)
    print(lower)
    print(upper)

