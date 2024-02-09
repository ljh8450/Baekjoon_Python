from sys import stdin

t = int(stdin.readline())

def check(f):
    temp = 0
    for i in range(2, int(f**0.5) + 1):
        if f%i == 0:
            return False
    return True

for _ in range(t):
    ans = 0
    n = int(stdin.readline())
    for i in range(2, n//2+1):
        x = i
        y = n-i
        if check(x) and check(y):
            ans += 1
            print(x, y)
    print(ans)