from sys import stdin
import heapq

n = int(stdin.readline())

queue = []
for _ in range(n):
    data = int(stdin.readline())
    if data != 0:
        heapq.heappush(queue, (abs(data), data))
    else:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue)[1])