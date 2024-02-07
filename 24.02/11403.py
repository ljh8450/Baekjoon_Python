# BFS
from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[0]* n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()
        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(n):
    bfs(i)

for i in visited:
    print(*i)

# DFS
def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[i] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')

    print()
    visited = [0 for _ in range(n)]