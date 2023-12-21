from sys import stdin

x = int(stdin.readline())
n = int(stdin.readline())
s = stdin.readline().strip()
p = "I"+"OI"*x
cnt = 0

def delete(s, n, x, p, cnt):
    t = n-2*x
    for i in range(0, t):
       if s[i: i+(2*x+1)] == p:
          t -= 2*x-1
          s = s[0:i] + s[i+2*x:t]
          cnt += 1
          return cnt
    n = 0

while len(s) > 2*n:
    delete(s, n, x, p, cnt)

print(cnt)