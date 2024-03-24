import sys

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        if check[i]:
            continue
        s.append(i)
        check[i] = True
        dfs(i+1)
        s.pop()
        check[i] = False

n, m = map(int, input().split())
check = [False] * (n+1)
s = []
dfs(1)