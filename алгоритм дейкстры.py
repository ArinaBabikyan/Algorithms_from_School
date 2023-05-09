# поиск кратчайшего пути во взешенном графе
# дан список смежности
n, s, f = map(int, input().split())
s-=1
f-=1
a = [list(map(int,input().split())) for i in range(n)]
D = [10**9] * n
seen = [False] * n
D[s] = 0
while False in seen:
    mi = 10**9
    kmi = 0
    for i in range(n):
        if seen[i] == False and D[i] < mi:
            mi = D[i]
            kmi = i
    if mi == 10**9:
        break
    seen[kmi] = True
    for i in range(n):
        if a[kmi][i] != -1 and a[kmi][i] != 0 and D[i] > mi + a[kmi][i]:
            D[i] = mi + a[kmi][i]
if D[f] == 10**9:
    print('-1')
else:
    print(D[f])