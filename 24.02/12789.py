from sys import stdin
from collections import deque

n = int(stdin.readline())
data = deque(list(map(int, stdin.readline().split())))
stack = deque([])

for i in range(n):
    if data[0] == min(data):
        data.popleft()
    else:
        if stack:
            if stack[-1] > data[0]:
                data.popleft()
            else:
                if stack[-1] < min(data):
                    stack.pop()
        else:
            if data[0] != min(data):
                stack.append(data.popleft())
            else:
                print("Sad")
    if len(data) <= 1 and len(stack) <= 1:
        print("Nice")
        break
    if not data and not stack:
        print("Nice")
        break