import sys
input = sys.stdin.readline
N = 3
MAX_ITER = 20
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return 1048576
    if dp[a][b][c]: return dp[a][b][c]
    if a < b < c:
       dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
       return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]
dp = [[[0] * MAX_ITER for _ in range(MAX_ITER)] for _ in range(MAX_ITER)]
a, b, c = map(int, input().split())
while True:
    stack = []
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break