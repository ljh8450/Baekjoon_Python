# queuestack -> queue or stack
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
temp = deque()

for i in range(n):
    if a[i] == 0:
        temp.appendleft(b[i])

for j in range(m):
    temp.append(c[j])
    print(temp.popleft(), end='')