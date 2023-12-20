from sys import stdin
from collections import deque

n = int(stdin.readline())

def split_int(data):
    return [int(i) for i in data]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    node = deque()
    node.append((x,y))

    num = 0

    while node:
        x, y = node.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y = dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif graph[nx][ny] == 1:
                num +=1
                graph[nx][ny] = 0
                node.append((nx, ny))
    return num
graph = list()
for i in range(n):
    data = stdin.readline().strip()
    graph.append(split_int(data))

visited = list()
ans = list()
for j in range(n*n):
    ans.append(bfs(0,0))

print(len(ans))
for i in ans:
    print(i)