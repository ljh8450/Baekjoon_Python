import sys
input = sys.stdin.readline

n = int(input())

def factorial(x):
    data = 1
    if x > 1:
        for i in range(2, x+1):
            data *= i
    return data

print(factorial(n))