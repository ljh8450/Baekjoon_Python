from sys import stdin

t = int(stdin.readline())

def calculater(m, n, x, y):
    k = x
    while k < m*n:
        if (k-x)%m == 0 and (k-y)%n == 0:
            return k
        k += m
    return -1

for _ in range(t):
    m, n, x, y = map(int, stdin.readline().split())
    print(calculater(m, n, x, y))