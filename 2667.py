from sys import stdin
from collections import deque

n = int(stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    n = len(graph)
    node = deque()
    node.append((x,y))
    graph[x][y] = 0
    visited[x][y] == True

    num = 1

    while node:
        x, y = node.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                num +=1
                graph[nx][ny] = 0
                visited[nx][ny] = True
                node.append((nx, ny))
    return num
graph = list()
visited = [[False] * n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input())))

ans = list()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(graph, i, j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)