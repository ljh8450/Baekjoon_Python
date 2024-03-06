import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = {}

for i in range(n):
    x = input().strip()
    temp = True
    if len(x) >= m:
        if x in data:
            data[x][0] += 1
        else:
            data[x] = [1, len(x)]
s = sorted(data.items(), key=lambda x:(-x[1][0], -x[1][1], x[0]))
for t in s:
    print(t[0])
