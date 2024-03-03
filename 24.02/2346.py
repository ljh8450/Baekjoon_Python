import sys
from collections import deque

input = sys.stdin.readline
# 변수 설정
n = int(input())
queue = deque(list(map(int, input().split())))
data = deque([x for x in range(1, n+1)])
index = 0
ans = list()
# 차례로 탐색
temp = queue.popleft()
ans.append(data.popleft())
for x in range(n-1):
    check = -1
    if temp < 0:
        temp = temp*(-1)
        check = 0
    else:
        check = 1
    for k in range(temp-1):
        if check > 0:
            queue.append(queue.popleft())
            data.append(data.popleft())
        else:
            queue.appendleft(queue.pop())
            data.appendleft(data.pop())
    if check == 1:
        ans.append(data.popleft())
        temp = queue.popleft()
    else:
        ans.append(data.pop())
        temp = queue.pop()

for a in ans:
    print(a, end=' ')