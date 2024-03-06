import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    a, b = input().strip().split()
    if a == 'ChongChong':
        data.append(b)
    elif b == 'ChongChong':
        data.append(a)
    elif a in data:
        data.append(b)
    elif b in data:
        data.append(a)

print(len(set(data))+1)