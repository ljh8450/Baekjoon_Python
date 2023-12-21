from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().strip()

def check(n, m, s):
    cnt = 1
    p = "I"+"OI"*n
    pl = len(p)
    for i in range(m-2*n):
        if s[i:i+pl] == p:
            cnt += 1
    return cnt

ans = check(n, m, s)
print(ans)