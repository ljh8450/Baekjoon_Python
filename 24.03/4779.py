def cut(n):
    if n == 1:
        return '-'
    else:
        left = cut(n//3)
        center = ' '*(n//3)
        return left + center + left
while True:
    try:
        n = int(input())
        ans = cut(3**n)
        print(ans)
    except:
        break