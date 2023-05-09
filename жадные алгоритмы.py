"""
Жадное свойство: в каждый момент времени каким является лучший выбор
С глобальной оптимизацией оно превращается в динамическое программирование
Жадный алгоритм очень быстрый

сдача: берем сначала побольше, потом идем меньше, пока возможно

жадные алгоритмы быстрые и простые
"""

#Выбор заявки
"""n = int(input())
li = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[1])
last = li[0][1]
cnt = 1
for i in li[1:]:
    if last <= i[0]:
        last = i[1]
        cnt += 1
print(cnt)"""
#проблема сапожника
"""n, k = list(map(int, input().split()))
li = sorted(list(map(int, input().split())))
su = 0
cnt = 0
for i in li:
    if su + i <= n:
        su += i
        cnt += 1
    else:
        break
print(cnt)"""
#journey
"""n, k = list(map(int, input().split()))
li = list(map(int, input().split()))
did = k
s = li[0]
li = (li[1:])[::-1]
cnt = 0
if k >= n:
    print(0)
else:
    i = 0
    while i != len(li):
        if did >= n:
            break
        elif did >= li[i]:
            cnt += 1
            n
            did = li[i] + k
            i = 0
        else:
            i += 1
    print(cnt) if did >= n else print(-1)
"""
#Большая политика

n = int(input())
li = (list(map(int, input().split())))
su = 0
while len(li) != 1:
    li = sorted(li)
    k = li[0] + li[1]
    su += k
    li[1] = k
    li.pop(0)
print(su)
