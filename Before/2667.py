from sys import stdin
from collections import deque

def bfs(graph, x, y, visited):
    n = len(graph)
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    visited[x][y] = True

    num_houses = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                num_houses += 1
                graph[nx][ny] = 0
                visited[nx][ny] = True
                queue.append((nx, ny))
                
    return num_houses

try:
    n = int(stdin.readline())
    graph = [list(map(int, input().strip())) for _ in range(n)]

    visited = [[False] * n for _ in range(n)]
    complexes = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                complexes.append(bfs(graph, i, j, visited))

    complexes.sort()

    print(len(complexes))
    for size in complexes:
        print(size)

except Exception as e:
    print(f"An error occurred: {e}")
