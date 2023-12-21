from sys import stdin

s = stdin.readline().strip()
n = int(stdin.readline())
p = "I"+"OI"*n
cnt = 0

def delete(s, n, p, cnt):

    t = len(s)-2*n
    for i in range(0, t):
       if s[i: i+(2*n+1)] == p:
          t -= 2*n-1
          s = s[0:i] + s[i+2*n:t]
          cnt += 1
          return cnt
    n = 0

while len(s) > 2*n:
    delete(s, n, p, cnt)

print(cnt)