from sys import stdin
n = int(stdin.readline())
#순서: 리스트형태 입력후 정렬된 집합
data = sorted(set(list(map(int, stdin.readline().strip().split()))))

for x in data:
    print(x, end=' ')
    