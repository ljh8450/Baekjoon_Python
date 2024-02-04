from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().strip()
index = 0
cnt = 0
ans = 0

while index < m - 1:
    if s[index:index+3] == "IOI":
        cnt += 1
        index += 2
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        cnt = 0
        index += 1

print(ans)