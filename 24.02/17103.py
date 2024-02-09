from sys import stdin

prime = []
check = [0]*1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    count = 0
    for i in prime:
        if i >= n:
            break
        if not check[n-i] and i <= n-i:
            count += 1

    print(count)