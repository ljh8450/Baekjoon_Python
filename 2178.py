from sys import stdin
from collections import deque

def split_int(input_int): #split int function
    return [int(i) for i in input_int]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                queue.append((nx, ny))
                data[nx][ny] = data[x][y] + 1 
    return data[n-1][m-1]


n, m = map(int, stdin.readline().split())
data = list()
for i in range(n):
    temp = stdin.readline().strip()
    data.append(split_int(temp))
print(dfs(0, 0))