# nCr = n!/((n-r)!*r!)
from math import factorial
for _ in range(int(input())):
    m, n = map(int, input().split())
    print(factorial(n)//(factorial(n-m)*factorial(m)))