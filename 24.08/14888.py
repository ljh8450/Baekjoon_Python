#앞에서부터 차례로 계산
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
bx = ['+' for x1 in range(bl[0])]+['-' for x2 in range(bl[1])]+['*' for x3 in range(bl[2])]+['/' for x4 in range(bl[3])]

max_result = float('-inf')
min_result = float('inf')

def calculate(operands, operators):
    result = operands[0]
    for i in range(1, len(operands)):
        if operators[i-1] == '+':
            result += operands[i]
        elif operators[i-1] == '-':
            result -= operands[i]
        elif operators[i-1] == '*':
            result *= operands[i]
        elif operators[i-1] == '/':
            if result < 0:
                result = -(-result//operands[i])
            else:
                result //= operands[i]
    return result

for p in set(permutations(bx)):
    result = calculate(al, p)
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)