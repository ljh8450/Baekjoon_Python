import sys
input = sys.stdin.readline
n = int(input())
ans = 0
data = list()

for i in range(n):
    x = input().strip()
    if x == 'ENTER' and i != 0:
        ans += len(set(data))-1
        data = list()
    data.append(x)
ans += len(set(data))-1
print(ans)