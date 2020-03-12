from collections import deque


if __name__ == "__main__":
    n = int(input())
    dq = deque()
    for i in range(n):
        '''
        cmd = str(input())
        if cmd.startswith("append"):
            v = int(cmd.split(" ")[1])
            dq.append(v)
        elif cmd.startswith("appendleft"):
            v = int(cmd.split(" ")[1])
            dq.appendleft(v)
        elif cmd.startswith("pop"):
            dq.pop()
        elif cmd.startswith("popleft"):
            dq.popleft()
        else:
            pass
        '''
        cmd = input().split()
        getattr(dq, cmd[0])(*[cmd[1]] if len(cmd) > 1 else [])

    print(*[i for i in dq])

