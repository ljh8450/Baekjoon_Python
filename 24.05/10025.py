import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cage = [0] * 1000001

for _ in range(n):
    g, x = map(int, input().split())
    cage[x] += g

max_sum = 0
current_sum = sum(cage[:2*k+1])
max_sum = max(max_sum, current_sum)

for i in range(1, 1000001-(2*k+1)):
    if i+2*k < 1000001:
        current_sum += cage[i+2*k] - cage[i-1]  # 오른쪽에서 추가하고 왼쪽에서 제거
        max_sum = max(max_sum, current_sum)

print(max_sum)
