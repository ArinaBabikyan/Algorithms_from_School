# Двоичный код
"""def dvo(n, s):
    if abs(n) == 1:
        return s + "1"
    return dvo(abs(n) // 2, s + str(n % 2))

n = int(input())
if not n:
    print(0)
else:
    print((n // (abs(n))) * int(''.join(reversed(list(dvo(n, ""))))))
"""

"""
def count(n):
    global ma
    if n % 10 > ma:
        ma = n % 10
    if len(str(n)) == 1:
        return
    count(int(str(n)[:-1]))


n = int(input())
ma = -1
count(n)
print(ma)"""

"""def dvo(path, cnt):
    global res
    cnt += 1
    for osn in li:
        res += (osn * (3 ** cnt))
        if res == n:
            return path
        dvo(path, cnt)
        path += osn
    return


n = int(input())
li = [1, 0, -1]
if n == 0:
    print(0)
else:
    num = int(n) // abs(int(n))
    if num < 0:
        n = n[1:]
    res = 0
    cnt = -1
    dvo(n, cnt)
    print(num * res)"""
"""
import sys
def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        if n in di:
            a = di1[n]
        else:
            a = G(n)
        if n in di1:
            b = di[n - 1]
        else:
            b = F(n - 1)
        return a + b
    if n > 2 and n % 2:
        if n + 1 in di1:
            a = di[n]
        else:
            a = F(n)
        if n - 2 in di:
            b = di1[n - 2]
        else:
            b = G(n - 2)
        return a + b


def G(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        if n - 3 in di1:
            a = di1[n - 3]
        else:
            a = F(n - 3)
        if n - 2 in di1:
            b = di1[n - 2]
        else:
            b = F(n - 2)
        return a + b
    if n + 1 in di1:
        a = di[n + 1]
    else:
        a = F(n + 1)
    if n in di:
        b = di[n - 1]
    else:
        b = G(n - 1)
    return a - b

sys.setrecursionlimit(100000)
di = {}
di1 = {}
for n in range(1, 120):
    di[n] = G(n)
    di1[n] = F(n)

"""

"""ef dvo(n):
    global s
    s += str(n % 3)
    if n < 2:
        return
    dvo(n // 3)


s = ''
n = int(input())
dvo(abs(n))
if n == 0:
    print(0)
else:
    li = list(map(int, s))
    if n // abs(n) == -1:
        li = list(map(lambda x: -x, li))
    for i in range(len(li) + 1):
        if i == len(li):
            break
        if i == len(s) - 1 and abs(li[i]) == 2 or abs(li[i]) == 3:
            li.append(0)
        if li[i] == 2:
            li[i] = '#'
            li[i + 1] += 1
        elif li[i] == 3:
            li[i] = 0
            li[i + 1] += 1
        elif li[i] == -2:
            li[i] = 1
            li[i + 1] -= 1
        elif li[i] == -3:
            li[i] = 0
            li[i + 1] -= 1
        if li[i] == -1:
            li[i] = '#'
    li = list(map(str, li))
    print(''.join(reversed(li)).lstrip('0'))"""

#степень двойки
"""def f(n):
    if n > 1:
        if n == 1:
            return True
        if n / 2 == n // 2 and f(n / 2):
            return True
    elif 1 > n > 0:
        if n == 1.0:
            return True
        if f(n * 2):
            return True
    if n == 1:
        return True


print("YES") if f(float(input())) else print("NO")"""
"""
import sys
def f(n, i=2):
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return f(n, i + 1)

sys.setrecursionlimit(20000)
print("YES") if f(int(input())) else print("NO")"""
#простые делители
"""
import sys


def rec(delit):
    global n, li
    if n % delit == 0 and all(list(map(lambda x: delit % x != 0 or delit == x, li))):
        n /= delit
        li.append(delit)
        print(delit, end=' ')
        rec(delit)
    if n == 1:
        return n
    else:
        rec(delit + 1)


n = int(input())
li = [2,]
sys.setrecursionlimit(100000)
if n == 1:
    print(1)
else:
    rec(2)"""
"""li = [int(input())]
while li[-1] != 0:
    li.append(int(input()))
print("{:.3f}".format(sum(li) / len(li)))"""


#EGE
"""def ways(start, finish):
    if start > finish or start == 15:
        return 0
    if start == finish:
        return 1
    return ways(start + 1, finish) + ways(start + 3, finish)

print(ways(2, 10) * ways(10, 20))"""
"""def ways(start, finish, flag=False):
    if start > finish:
        return 0
    if start == finish:
        return 1
    if flag:
        return ways(start + 1, finish) + ways(start + 2, finish)
    return ways(start + 1, finish) + ways(start + 2, finish) + ways(start * 2, finish, True)


print(ways(1, 15))
"""
"""from functools import lru_cache

@lru_cache
def F(n):
    if n <= 15:
        return 2 * n ** 2 + 4 * n + 3
    if n > 15 and n % 3 == 0:
        return F(n - 1) + n * n + 3
    if n > 15 and n % 3:
        return F(n - 2) + n - 6
cnt = 0
for i in range(1, 1001):
    f = True
    for x in str(F(i)):
        if int(x) % 2 == 0:
            f = False
    if f:
        cnt += 1
print(cnt)"""
"""from functools import lru_cache

@lru_cache
def F(n):
    if n > 25:
        return 2 * n ** 3 + 1
    else:
        return F(n + 2) + 2 * F(n + 3)
cnt = 0
for i in range(1, 1001):
    if F(i) % 11 == 0:
        cnt += 1
print(cnt)
"""
#cp
"""from functools import lru_cache

@lru_cache
def F(n):
    if n <= 5:
        return n + 15
    if n > 5 and n % 2 == 0:
        return F(n // 2) + n * n * n - 1
    if n > 5 and n % 2:
        return F(n - 1) + 2 * n ** 2 + 1
cnt = 0
for i in range(1, 1001):
    k = F(i)

    if str(k).count("8") >= 2:
        cnt += 1
print(cnt)"""
"""from functools import lru_cache

@lru_cache
def F(n):
    if n < 4:
        return n - 1
    if n >= 4 and n % 3 == 0:
        return n + 2 * F(n - 1)
    if n >= 4 and n % 3:
        return F(n - 2) + F(n - 3)

print(F(25))
print(sum(list(map(int, list(str(F(25)))))))"""
"""
from functools import lru_cache

@lru_cache
def F(n):
    if n < 3:
        return 1
    if n > 2 and sum(list(map(int, list(str(n))))) % 2 == 0:
        return F(n - 1) - F(n - 2)
    if n > 2 and sum(list(map(int, list(str(n))))) % 2:
        return F(n - 1) + F(n // 2)


print(F(100))"""
"""from functools import lru_cache
import sys

@lru_cache
def F(n):
    if n > 10000:
        return n - 10000
    elif n >= 1:
        return F(n + 1) + F(n + 2)
sys.setrecursionlimit(1000000)
print(F(12345) * (F(10) - F(12)) / F(11) + F(10101))
"""
"""from functools import lru_cache
@lru_cache
def ways(start, finish, flag=False):
    if start > finish or start == 23:
        return 0
    if start == finish:
        return 1
    if flag:
        return ways(start + 2, finish) + ways(start * 2, finish)
    return ways(start + 1, finish, True) + ways(start + 2, finish) + ways(start * 2, finish)


print(ways(3, 11) * ways(11, 79))"""
"""from functools import lru_cache
import sys
@lru_cache
def ways(start, count=0):
    global li
    if count == 11:
        li.append(start)
        return
    return ways(start - 2, count + 1), ways(start * (-3), count + 1)

li = []
print(li)"""
"""from functools import lru_cache
import sys
@lru_cache
def ways(start, count=0):
    global li
    if count == 11:
        li.append(start)
        return
    return ways(start - 2, count + 1), ways(start * (-3), count + 1)

li = []
print(li)"""
from functools import lru_cache
@lru_cache
def ways(start, finish, flag=False):
    global cnt
    if start > finish or start == 23:
        return 0
    if start == finish:
        if flag:
            cnt += 1
        return 1
    if flag:
        return ways(start + 2, finish) + ways(start * 2, finish)
    return ways(start + 1, finish, True) + ways(start + 2, finish) + ways(start * 2, finish)


cnt = 0
a = ways(3, 11)
print(cnt * ways(11, 79, True))
print((a - cnt) * ways(11, 79) + cnt * ways(11, 79, True))
