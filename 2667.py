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
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny]:
                graph[x][y] = 0
                visited[x][y] = 1
                num += 1
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
for i in len:
    print(i)