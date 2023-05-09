# Алгоритм Флойда-Уоршелла
# Кратчайший путь между всеми парами вершин за один проход О(n^3)
# Работает на основе весовой матрицы, где отсутсвие ребер обозначается +беск
""""n = int(input())
vvod = [list(map(int, input().split())) for i in range(n)]
li = [[0 for j in range(n)] for i in range(n)]
flag = True
mi1 = 10e10
for i in range(n):
    for j in range(n):
        if vvod[i][j] < 0:
            flag = False
        if i == j:
            li[i][j] = 0
        else:
            li[i][j] = vvod[i][j]
    if mi1 > min(li[i]):
        mi1 = min(li[i])
for k in range(n):
    for i in range(n):
        for j in range(n):
            li[i][j] = min(li[i][j], li[i][k] + li[k][j])
mi = 1000000
for i in range(n):
    for j in range(n):
        if not li[i][j]:
            li[i][j] = 1000000
    if mi > min(li[i]):
        mi = min(li[i])
if mi < mi1:
    print(-1)
else:
    print(mi)"""
"""
li = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            li[i][j] = 0
        elif li[i][j] == -1:
            li[i][j] = 10e9
        else:
            li[i][j] = vvod[i][j]
print(li)
for k in range(n):
    for i in range(n):
        for j in range(n):
            li[i][j] = min(li[i][j], li[i][k] + li[k][j])
ma = -1
for i in range(len(li)):
    if ma < max(li[i]):
        ma = max(li[i])
print(ma)"""
n, m = list(map(int, input().split()))
li1 = [list(map(int, input().split())) for i in range(m)]
vvod = [[0 for j in range(n)] for i in range(n)]
for i in li1:
    vvod[i[0] - 1][i[1] - 1] = i[2]
li = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            li[i][j] = 0
        elif vvod[i][j] == 0:
            li[i][j] = 10e9
        else:
            li[i][j] = vvod[i][j]
for k in range(n):
    for i in range(n):
        for j in range(n):
            li[i][j] = min(li[i][j], li[i][k] + li[k][j])
ma = -1
for i in range(len(li)):
    if max(li[i]) != 10e9:
        if ma < max(li[i]):
            ma = max(li[i])
print(ma) if ma != -1 else print(0)
