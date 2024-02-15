from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
D = deque([])

for _ in range(n):
    data = input().strip()
    if data[0] == '1':
        x, y = data.split()
        D.appendleft(int(y))
    elif data[0] == '2':
        x, y = data.split()
        D.append(int(y))
    elif data[0] == '3':
        if D:
            print(D.popleft())
        else:
            print(-1)
    elif data[0] == '4':
        if D:
            print(D.pop())
        else:
            print(-1)
    elif data[0] == '5':
        print(len(D))
    elif data[0] == '6':
        if not D:
            print(1)
        else:
            print(0)
    elif data[0] == '7':
        if D:
            print(D[0])
        else:
            print(-1)
    elif data[0] == '8':
        if D:
            print(D[-1])
        else:
            print(-1)