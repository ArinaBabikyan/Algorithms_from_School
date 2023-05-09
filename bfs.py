"""
поиск в ширину - метод обхода графа в ширину
при каждом нвоом шаге посещаются вершины, расстояние от которых до начальной на единицу больше предыдущего
для хранения временных данных испольуется очередь
сложность O(m + n)

"""
"""список смежности дан
def bfs(v):
    queue = []
    used[v] = 1
    queue.append(v)
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in g[v]:
            if not used[i]:
                used[i] = 1
                queue.append(i)
"""

"""применение:
1. волновой алгоритм поиска пути в лабиринте
2. поиск кратчайшего пути
3. поиск компонент связанности"""

# пересадки два
"""def dfs(v, path):
    if v in path or len(path) > k + 2:
        return
    path.append(v)
    if v == finish and len(path) == k + 2:
        res.append(' '.join(map(str, path)))
    else:
        for j in range(n):
            if G[v - 1][j] == '1':
                dfs(j + 1, path)
    path.pop()


n = int(input())
G = [input().split() for i in range(n)]
res = []
start, finish = list(map(int, input().split()))
k = int(input())
dfs(start, [])
print(len(res))
for i in res:
    print(i)"""

"""def dfs(v, path):
    if v in path:
        return
    if path:
        path2.append(int(G[path[-1] - 1][v - 1]))
    path.append(v)
    if v == finish:
        res.append(path[:])
    else:
        for j in range(n):
            if G[v - 1][j] != '0' and sum(path2) + int(G[v - 1][j]) <= mini:
                dfs(j + 1, path)
    path.pop()
    if path2:
        path2.pop()


n = int(input())
G = [input().split() for i in range(n)]
res = []
start, finish = list(map(int, input().split()))
su = int(input())
path2 = []
dfs(start, [])
print(len(res))
res = sorted(res, key=lambda x: (len(x), x))
for i in res:
    print(*i)"""


# Один конь


def bfs(node):
    used = set()
    queue = []
    used.add(node)
    queue.append((node, [node]))
    while queue:
        m, way = queue.pop()
        node = m
        graph = [(node[0] + 2, node[1] + 1), (node[0] + 2, node[1] - 1), (node[0] - 2, node[1] - 1), (node[0] - 2, node[1] + 1), (node[0] + 1, node[1] + 2),
                 (node[0] + 1, node[1] - 2), (node[0] - 1, node[1] + 2), (node[0] - 1, node[1] - 2)]
        print(graph, node)
        if (x2, y2) in graph:
            print(len(way))
            for i in way:
                print(*i)
            print(x2, y2)
            break
        for i in graph:
            if any([j for j in i if j < 0]) or any([j for j in i if j > n or j == x1 or j == x2]):
                continue
            if i not in way and (i[1], i[0]) not in way:
                used.add(i)
                queue.insert(0, (i, way + [i]))

n = int(input())
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
if (x1, y1) == (x2, y2):
    print(0)
else:
    bfs((x1, y1))

# Табличка
"""def bfs(v):
    queue = []
    used[v] = 1
    queue.append(v)
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in g[v]:
            if not used[i]:
                used[i] = 1
                queue.append(i)"""
