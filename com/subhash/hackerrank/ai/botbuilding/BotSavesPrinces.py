
def displayPathtoPrincess(n, grid):
    mX = int(n / 2) + 1
    mY = mX

    # print("{}, {}".format(mX, mY))

    for i in range(1, n + 1):
        line = grid[i-1]
        lineLne = len(line)
        if line[0] == 'p':
            pX = 1
            pY = i
        elif line[lineLne - 1] == 'p':
            pX = n
            pY = i

    # print("{}, {}".format(pX, pY))

    xDir = "LEFT" if pX < mX else "RIGHT"
    yDir = "UP" if pY < mY else "DOWN"

    for i in range(mX, n):
        print(yDir)

    for i in range(mX, n):
        print(xDir)


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)

