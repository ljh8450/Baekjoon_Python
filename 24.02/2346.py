import sys
from collections import deque

input = sys.stdin.readline
# 변수 설정
n = int(input())
data = deque(list(map(int, input().split())))
index = 0
ans = list()
# 차례로 탐색
for x in range(n):
    if len(data) <= 1:
        ans.append(data.popleft())
        break
    ans.append(index+1)
    if index >= len(data):
        index = index%len(data)
    temp = index
    for y in range(data[index]):
        # 탐색 플로우: +면 popleft&append/ -면 pop&appendleft
        if data[index] >= 0:
            data.append(data.popleft())
            temp += 1
        else:
            data.appendleft(data.pop())
            temp -= 1
    if index < 0:
        temp += n-1
    data.popleft()
    index = temp
for t in ans:
    print(t, end=' ')