import sys
input = sys.stdin.readline

n = int(input())
data = [0, 0, 0]
s = [0, 0, 0]

for i in range(n):
    data = list(map(int, input().split()))
    s[0] += data[0]
    s[1] += data[1]
    s[2] += data[2]

g = list(map(int, input().split()))
ans = abs(sum(g)-sum(s)//n)

print(ans)