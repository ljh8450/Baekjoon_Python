import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def merge_sort(a, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    global cnt, res
    i = p
    j = q+1
    tmp = []
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        a[i] = tmp[t]
        cnt += 1
        if cnt == k:
            res = a[i]
            break
        i += 1
        t += 1

a = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(a, 0, n-1)
print(res)