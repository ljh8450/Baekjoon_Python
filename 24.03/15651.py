import sys
input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return 0
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()

n, m = map(int, input().split())
s = []
dfs(1)