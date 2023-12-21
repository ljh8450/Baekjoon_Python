from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().strip()

def check(n, s):
    cnt = 0
    p = "I"+"OI"*n
    pl = len(p)
    for i in range(len(s)-pl+1):
        if s[i:i+pl] == p:
            cnt += 1
    return cnt

ans = check(n, s)
print(ans)