"""L = 0; R = N # начальный отрезок
while L < R-1:
    c = (L+R) // 2  # нашли середину
    if X < A[c]:  # сжатие отрезка
        R = c
    else: L = c
if A[L] == X:
    print ( "A[", L, "]=", X, sep = "" )
else:
    print ( "Не нашли!" )"""
#двоичный
"""n, k = list(map(int, input().split()))
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
for X in li2:
    L = 0
    R = n  # начальный отрезок
    while L < R - 1:
        c = (L + R) // 2  # нашли середину
        if X < li1[c]:  # сжатие отрезка
            R = c
        else:
            L = c
    if li1[L] == X:
        print("YES")
    else:
        print("NO")"""
#сложность
"""n = int(input())
li1 = [i for i in range(1, n + 1)]
ma = 0
for X in li1:
    cnt = 0
    L = 0
    R = n
    while L < R - 1:
        cnt += 1
        c = (L + R) // 2  # нашли середину
        if X < li1[c]:  # сжатие отрезка
            R = c
        else:
            L = c
    if ma < cnt:
        ma = cnt
print(ma)"""
"""n, k = list(map(int, input().split()))
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
for X in li2:
    L = 0
    R = n - 1
    mi = 999999999
    while L < R - 1:
        c = (L + R) // 2
        if X < li1[c]:
            R = c
        else:
            L = c
    if abs(li1[L] - X) > abs(li1[R] - X):
        print(li1[R])
    else:
        print(li1[L])"""
"""n = int(input())
for X in range(n + 1):
    cnt = 0
    L = 0
    R = n
    while L < R - 1:
        cnt += 1
        c = (L + R) / 2  # нашли середину
        if X < c:  # сжатие отрезка
            R = c
        else:
            L = c
print(c)"""
#провода
"""n, k = list(map(int, input().split()))
li = [int(input()) for i in range(n)]
l = 0
r = sum(li)
mid = 1
while l < r - 1:
    mid = (l + r) // 2
    cnt = 0
    for i in li:
        cnt += i // mid
    if cnt < k:
        r = mid
    else:
        l = mid
print(l)"""
#коровы в стойла
n, k = list(map(int, input().split()))
li = list(map(int, input().split()))
l = 2
r = li[-1] - l
while l < r - 1:
    mid = (l + r) // 2
    cnt = 1
    stage = 0
    for i in range(n):
        if li[i] - li[stage] >= mid:
            stage += 1
            cnt += 1
    if cnt >= k:
        l = mid + 1
    else:
        r = mid
print(cnt)
