#структура данных деки

import collections
import math
import sys
"""iterable = '123'
maxlen = 5
x = 'b'
start, stop = 1, 3
dq = collections.deque([iterable[, maxlen],])
dq.append(x)
dq.appendleft(x)
dq.copy()
dq.clear()
dq.count(x)
dq.extend(iterable)
dq.extendleft('ab')#dq = ['b', 'a', ...] добавляет уже реверснутый итератор
dq.index(x[, start[, stop]])
dq.pop()#справа
dq.popleft()
dq.rotate(2) #на n вправо^^^два справа снял и поставил в начало
dq.maxlen#возвращает длину"""

#задачи
#2 реверс массива
"""dq = []
with open('output.txt', 'w') as f:
    cnt = 1
    for i in open('input.txt'):
        if cnt == 1:
            cnt += 1
            continue
        i = i.split()
        for j in range(len(i) - 1, -1, -1):
            if i[j]:
                print(i[j], file=f, end=' ')
"""
#Моделирование стека
"""
with open('output.txt', 'w') as f:
cnt = 1
dq = collections.deque()
flag = True
for i in open('input.txt'):
    if '+' in i:
        dq.append(i.strip('+\n'))
    elif dq:
        dq.pop()
    else:
        flag = False
if dq and flag:
    print(*dq, file=f)
elif flag:
    print('EMPTY', file=f)
else:
    print('ERROR', file=f)"""

#Скобочное выражение
"""a = input()
dq = collections.deque()
di = [('(', ')'), ('{', '}'), ('[', ']'), ('<', '>')]
for i in a:
    if i in '(){}[]<>':
        if dq and (dq[-1], i) in di:
            dq.pop()
        else:
            dq.append(i)
if len(dq) == 0:
    print('YES')
else:
    print("NO")"""
#Мини-Форт
"""dq = collections.deque()
flag = True
for i in open('input.txt'):
    if i.strip().isdigit():
        dq.append(i.strip())
    else:
        i = i.strip()
        if i == 'DROP':
            if not dq:
                flag = False
                break
            dq.pop()
        if i == 'SWAP':
            if len(dq) < 2:
                flag = False
                break
            a = dq.pop()
            b = dq.pop()
            dq.extend([a, b])
        if i == 'DUP':
            if not dq:
                flag = False
                break
            dq.append(dq[-1])
        if i == 'OVER':
            if len(dq) < 2:
                flag = False
                break
            dq.append(dq[-2])
        if i == '+':
            if len(dq) < 2:
                flag = False
                break
            a = dq.pop()
            b = dq.pop()
            a, b = int(a), int(b)
            dq.append(a + b)
        if i == '-':
            if len(dq) < 2:
                flag = False
                break
            a = dq.pop()
            b = dq.pop()
            a, b = int(a), int(b)
            dq.append(b - a)
        if i == '*':
            if len(dq) < 2:
                flag = False
                break
            a = dq.pop()
            b = dq.pop()
            a, b = int(a), int(b)
            dq.append(a * b)
        if i == '/':
            if len(dq) < 2:
                flag = False
                break
            a = dq.pop()
            b = dq.pop()
            if not int(a):
                flag = False
                break
            a, b = int(a), int(b)
            dq.append(b // a)
with open('output.txt', 'w') as f:
    if dq and flag:
        print(*dq, file=f)
    elif not flag:
        print("ERROR", file=f)
    else:
        print('EMPTY', file=f)"""
#1 постфиксная запись
"""a = input().split()
s1 = '+-/*'
f = True
dq = collections.deque()
for i in range(len(a)):
    if a[i].isdigit():
        dq.append(a[i])
    if a[i] in s1 and len(dq) >= 2:
        x2 = int(dq.pop())
        x1 = int(dq.pop())
        if a[i] == '/':
            dq.append(str(x1 // x2))
        if a[i] == '+':
            dq.append(str(x1 + x2))
        if a[i] == '-':
            dq.append(str(x1 - x2))
        if a[i] == '*':
            dq.append(str(x1 * x2))
    elif a[i] in s1:
        f = False
        break
if len(dq) != 1 or not f:
    print("ERROR")
else:
    print(dq[0])"""
#Постфиксная запись с функциями
"""a = input().split()
li = list(map(lambda x: x.split('='), sys.stdin.readlines()))
s1 = '+-/*'
s2 = ['sin', 'cos', 'abs', 'sqrt']
f = True
dq = collections.deque()
for i in range(len(a)):
    if a[i].isdigit():
        dq.append(float(a[i]))
    elif [j for j in li if j[0] == a[i]]:
        dq.append(float(" ".join([j[1].strip() for j in li if a[i] == j[0]])))
    elif a[i] in s1 and len(dq) >= 2:
        x2 = dq.pop()
        x1 = dq.pop()
        if a[i] == '/':
            dq.append((x1 / x2))
        if a[i] == '+':
            dq.append((x1 + x2))
        if a[i] == '-':
            dq.append((x1 - x2))
        if a[i] == '*':
            dq.append((x1 * x2))
    elif dq and a[i] in s2:
        if a[i] == 'abs':
            x1 = dq.pop()
            dq.append((abs(x1)))
        if a[i] == 'sin':
            x1 = dq.pop()
            dq.append((math.sin(x1)))
        if a[i] == 'cos':
            x1 = dq.pop()
            dq.append((math.cos(x1)))
        if a[i] == 'sqrt':
            x1 = dq.pop()
            dq.append((math.sqrt(x1)))
    elif a[i] in s1 or a[i] in s2:
        f = False
        break
if len(dq) != 1 or not f:
    print("ERROR")
else:
    print(str("{:.3f}".format(dq[0])))"""
#Из инфиксной в постфиксную
"""a = ''.join(input().split())
s1 = '-+*/'
dq = collections.deque()
s = ''
li1 = []
li2 = []
cnt = 0
last = ''
for i in range(len(a)):
    if a[i] in s1:
        dq.append(s)
        dq.append(a[i + 1:])
        dq.append(a[i])
        s = ''
        last = a[i + 1:]
        break
    if a[i].isdigit():
        s += a[i]
print(dq)
print(last)
while True:
    for i in range(len(last)):
        if last[i] in s1:
            dq.append(s)
            dq.append(last[i + 1:])
            dq.append(last[i])
            s = ''
            last = last[i + 1:]
            break
        if last[i].isdigit():
            s += last[i]
    print(len(dq))
    if len(dq) == 15:
        break
print(dq)
for i in range(len(dq)):
    if (i + 2) % 3:
        print(dq[i], end=' ')"""
#вычисление выражение с переменными
"""a = input()
di = {}
di1 = {'sin': math.sin, 'cos': math.cos, 'sqrt': math.sqrt}
for i in list(map(lambda x: x.strip().split('='), sys.stdin.readlines())):
    di[i[0]] = int(i[1])
print('{:.3f}'.format(eval(a, di, di1)))"""
#управление очередью
"""dq = collections.deque()
with open('input.txt') as f, open('output.txt', 'w') as f1:
    flag = True
    f = f.readlines()
    for i in f:
        i = i.strip()
        if '+' in i:
            dq.appendleft(i[1:])
        elif '-' == i:
            if not dq:
                flag = False
                break
            else:
                dq.pop()
        else:
            flag = False
            break
    if not flag:
        print("ERROR", file=f1)
    elif not dq:
        print("EMPTY", file=f1)
    else:
        print(' '.join(reversed(list(dq))), file=f1)"""
#только 2, 3, 5
"""n = int(input())
st1, st2, st3 = collections.deque(), collections.deque(), collections.deque()
st1.append(2)
st2.append(3)
st3.append(5)
x = 2
for i in range(n):
    x = min(st1[0], st2[0], st3[0])
    print(x, end=' ')
    if st1[0] == x:
        st1.popleft()
    if st2[0] == x:
        st2.popleft()
    if st3[0] == x:
        st3.popleft()
    st1.append(x * 2)
    st2.append(x * 3)
    st3.append(x * 5)"""
#заливка
"""with open('input.txt') as f, open('output.txt', 'w') as f2:
    n, m = list(map(int, f.readline().split()))
    x, y = list(map(int, f.readline().split()))
    colorto = int(f.readline())
    a = list(map(lambda x: list(map(int, x.split())), f.readlines()))
    xmax = len(a[0])
    ymax = len(a)
    st = collections.deque()
    st.append((x, y))
    color = a[y][x]
    cnt = 0
    f = True
    li = []
    for i in a:
        if len(set(i)) != 1:
            f = False
        else:
            li.append(i[0])
    if len(set(li)) != 1 or (len(set(li)) == 1 and li[0] != colorto):
        while st:
            x, y = st.popleft()
            if a[y][x] == color:
                a[y][x] = colorto
                if x > 0:
                    st.append((x - 1, y))
                if x < xmax - 1:
                    st.append((x + 1, y))
                if y > 0:
                    st.append((x, y - 1))
                if y < ymax - 1:
                    st.append((x, y + 1))
                cnt += 1
    print(cnt, file=f2)
    for i in a:
        for j in i:
            print(j, end=' ', file=f2)
        print(file=f2)
"""
#путьб в лабиринте 2
"""with open('input.txt') as f:
    n, m = f.readline().strip().split()
    x1, y1 = f.readline().strip().split()
    x2, y2 = f.readline().strip().split()
    matrix = list(map(lambda x: x.strip(), f.readlines()))
    rn = [x1, y1]
    length = 0
    while matrix[rn[0] + 1][rn[1] + 1] == '.':
        rn = [x1 + 1, y1 + 1]
        length += 1
    while
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if"""
#Считалка
"""n, k = list(map(int, input().split()))
li = [i for i in range(1, n + 1)]
last = 0
while li:
    for i in range(k):
        if last == len(li):
            last = 0
        last += 1
    last -= 1
    print(li.pop(last), end=' ')"""
#Сортировщик поездов
"""with open('input.txt') as f, open('output.txt', 'w') as f2:
    n = int(f.readline().strip())
    li = list(map(lambda x: [int(x.strip().split()[0]), x.strip().split()[1]], f.readlines()))
    li = sorted(li, key=lambda x: x[0])
    for i in li:
        print(*i, file=f2)"""
#Колода карт
dq = collections.deque()
with open('input.txt') as f1, open('output.txt', 'w') as f2:
    f = True
    for i in f1:
        i = i.strip()
        if '+' in i:
            if i[1:len(i)] not in dq:
                dq.append(i[1:len(i)])
            else:
                f = False
                print("ERROR", file=f2)
                break
        if '^' in i:
            if dq:
                dq.pop()
            else:
                f = False
                print("ERROR", file=f2)
                break
        if '#' in i:
            if i[1:len(i)] not in dq:
                dq.appendleft(i[1:len(i)])
            else:
                f = False
                print("ERROR")
                break
        if '/' in i:
            if dq:
                dq.popleft()
            else:
                f = False
                print('ERROR', file=f2)
                break
    if f:
        if dq:
            for i in reversed(dq):
                print(i, file=f2, end=' ')
        else:
            print('EMPTY', file=f2)

