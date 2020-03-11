N, M = map(int, input().split())

# print("N: {}, M: {}", N, M * 2)

for i in range(N):
    if i < (N // 2):
        # print("upper half")
        print(("-" * (((M-3)//2) - (3 * (i)))) + (".|." * (2 * i + 1)) + ("-" * (((M-3)//2) - (3 * (i)))))
    elif i == (N // 2):
        print(("-" * ((M-7)//2)) + "WELCOME" + ("-" * ((M-7)//2)))
    else:
        # print("lower half")
        print(("-" * (((M-3)//2) - (3 * (N - 1 - i)))) + (".|." * (2 * (N - 1 - i) + 1))
              + ("-" * (((M-3)//2) - (3 * (N - 1 - i)))))
