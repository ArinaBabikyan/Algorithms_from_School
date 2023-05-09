# bfs algorigthm
"""def bfs(used, graph, node): #function for BFS
    used.append(node)
    queue.append(node)
    while queue:          # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in used:
                print(queue)
                used.append(neighbour)
                queue.append(neighbour)"""
# dfs algo
"""
visited = [False for i in range(self.V)]
stack = []

stack.append(start)

while (len(stack)):
    s = stack[-1]
    stack.pop()
    if (not visited[s]):
        print(s, end=' ')
        visited[s] = True
    for node in self.adj[s]:
        if (not visited[node]):
            stack.append(node)"""
#Количество дорог
"""n = int(input())
di = []
li = [list(map(int, input().split())) for i in range(n)]
su = 0
li1 = list(map(int, input().split()))
for i in range(1, len(li1)):
    if li[li1[i - 1] - 1][li1[i] - 1]:
        su += li[li1[i - 1] - 1][li1[i] - 1]
    else:
        su = 0
        break
print(su)"""
"""def dfs(v):
    #smth we need
    used[v] = 1
    for i in g[v]:
        if not used[i]:
            dfs(i)


used = [0] * len(g)
dfs(0)
g = {} #dictionary список смдености"""
#how many each road
"""n = int(input())
di = []
li = [list(map(int, input().split())) for i in range(n)]
cnt1 = 0
cnt2 = 0
for i in range(n):
    for j in range(i, n):
        if li[i][j] == li[j][i] and li[i][j]:
            cnt1 += 1
        else:
            if li[i][j]:
                cnt2 += 1
            if li[j][i]:
                cnt2 += 1
print(cnt2, cnt1)"""
# связанность
"""def dfs(v):
    used[v - 1] = 1
    for i in g[v]:
        if not used[i - 1]:
            dfs(i)
    return used


n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
g = {}
for i in range(len(li)):
    g[i + 1] = []
    for j in range(len(li[i])):
        if li[i][j]:
            g[i + 1].append(j + 1)
used = [0] * n
cnt = 1
li1 = dfs(cnt)
cnt2 = 0
while sum(li1) != n:
    cnt = li1.index(0) + 1
    li1 = dfs(cnt)
    cnt2 += 1
print(cnt2 + 1)



"""
#Изоляция
"""
n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
f = False
for i in range(len(li)):
    if sum([max(li[i][j], li[j][i]) for j in range(n)]) == 0:
        f = True
        print(i + 1, end=' ')
if not f:
    print(0)"""

"""def dfs(v, used, li):
    used[v - 1] = 1
    li.append(v)
    for i in g[v]:
        if not used[i - 1]:
            if len(li) == k + 1 and v not in g[li[0]]:
                print(v, li[0])
                print(li)
                return li
            dfs(i, used, li)
    return 0


n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
k = int(input())
g = {}
for i in range(len(li)):
    g[i + 1] = []
    for j in range(len(li[i])):
        if li[i][j]:
            g[i + 1].append(j + 1)
print(g)
for i in range(1, 1 + n):
    li = []
    used = [0] * n
    li = dfs(i, used, li)

"""

"""
n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
k = int(input())
g = {}
for i in range(len(li)):
    g[i + 1] = []
    for j in range(len(li[i])):
        if li[i][j]:
            g[i + 1].append(j + 1)
print(g)
for i in range(1, n + 1):
    used = []
    queue = []
    bfs(used, g, i)"""


#вернуться за k перелетов
"""def dfs(num, lvl, start):
    global ways
    used[num] = True
    if lvl < maxi - 1:
        for i in g[num + 1]:
            if not used[i - 1]:
                dfs(i - 1, lvl + 1, start)
    elif lvl == maxi - 1 and start + 1 in g[num + 1] and used[start]:
        ways += 1
    used[num] = False

n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
g = {}
for i in range(len(li)):
    g[i + 1] = []
    for j in range(len(li[i])):
        if li[i][j]:
            g[i + 1].append(j + 1)
maxi = int(input())
ways = 0
for i in range(n):
    used = [False] * n
    dfs(i, 0, i)
    for k, v in g.items():
        if i + 1 in v:
            g[k].pop(g[k].index(i + 1))
print(ways)"""
"""def dfs(num, lvl, start):
    global ways, li
    used[num] = True
    if lvl < maxi:
        for i in g[num + 1]:
            if not used[i - 1]:
                if lvl == maxi - 1 and i not in g[start + 1] and i in g[num + 1] and (i, start + 1) not in li:
                    li.append([start + 1, i])
                elif lvl > maxi - 2:
                    continue
                dfs(i - 1, lvl + 1, start)
    used[num] = False

n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
g = {}
for i in range(len(li)):
    g[i + 1] = []
    for j in range(len(li[i])):
        if li[i][j]:
            g[i + 1].append(j + 1)
li = [[]]
maxi = int(input())
ways = 0
for i in range(n):
    used = [False] * n
    dfs(i, 0, i)
printed = []
li.pop(0)
if len(li):
    for i in li:
        if i[::-1] in li and i not in printed:
            print(*i)
            printed.append(i[::-1])
else:
    print(0)"""


"""def dfs(v, path):
    for j in range(n):
        if G[v - 1][j] == 1:
            dfs(j + 1, path)



n = int(input())
G = [list(map(int, input().split())) for i in range(n)]
res = []
start, finish = list(map(int, input().split()))
dfs(start, [])
print(len(res))
res = sorted(res, key=lambda x: (len(x), x))
for i in res:
    print(*i)"""


"""def dfs(v, path):
    global res
    if v in path or len(path) > k + 2:
        return
    path.append(v)
    if v == finish and len(path) == k + 2:
        res.append([path[0], path[-1]])
    else:
        for j in range(n):
            if G[v - 1][j] == '1':
                dfs(j + 1, path)
    path.pop()


n = int(input())
G = [input().split() for i in range(n)]
res = []
k = int(input())
for i in range(1, n):
    start = i
    for j in range(i + 1, n + 1):
        finish = j
        if G[start - 1][finish - 1] == '0':
            dfs(start, [])
if res:
    for i in res:
        print(*i)
else:
    print(0)"""

"""
def dfs(s, v, x):
    if x == k:
        if s < v:
            ans.add((s + 1, v + 1))
        return
    used[v] = 1
    for u in range(n):
        if g[v][u] and not used[u]:
            dfs(s, u, x + 1)
    used[v] = 0

n = int(input())
g = []
ans = set()

for i in range(n):
    g.append(list(map(int, input().split())))
k = int(input())

for i in range(n):
    used = [0] * n
    dfs(i, i, -1)

ans = sorted(ans)

if len(ans) > 0:
    for p in ans:
        print(p[0], p[1])
else:
    print(0)"""

