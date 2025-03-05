import sys
input = sys.stdin.readline

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
while True:
    if graph[x][y] == 0:
        graph[x][y] = 2
        answer += 1
    for i in range(4):
        d = (d - 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
            break
    else:
        nx, ny = x - dx[d], y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                print(answer)
                break
            else:
                x, y = nx, ny
