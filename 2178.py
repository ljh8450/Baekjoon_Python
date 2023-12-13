from sys import stdin

def split_int(input_int): #split int function
    return [int(i) for i in input_int]


n, m = map(int, stdin.readline().split())
data = list()
for i in range(n):
    temp = stdin.readline().strip()
    data.append(split_int(temp))
print(data)   