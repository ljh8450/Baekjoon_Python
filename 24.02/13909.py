from sys import stdin

n = int(stdin.readline())
data = [0]*(n+1)

def func(x, n):
    for k in range(x, n+1, x):
        if data[k-1] == 1:
            data[k-1] = 0
        else:
            data[k-1] = 1
for i in range(1, n+1):
    func(i, n)

print(data.count(1))