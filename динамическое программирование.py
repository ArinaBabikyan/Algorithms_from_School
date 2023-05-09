"""
динамическое программирование - это способ решения сложных задач путем сведения их к более простмы задачам того же типа
Задача: найти количесвто цепочек, не имеюших двух единиц подряд.
Это числа фиббоначи. тк если ноль то задача n - 1, если единица то n - 2
"""
"""
задача: 
n молока; 1, 5 и 6 литров. минимальноео количество бидонов
kn - это минимальное число бидонов для n литров
kn = 1 + k(индекс)(n - 1)
kn = 1 + k(индекс)(n - 5)
kn = 1 + k(индекс)(n - 6)
kn = 1 + min(k(n-1), k(n-5), k(n-6))
k20 = 1 + min(k19, k15, k14)


    строим таблицу
0 1 2 3 4 5 6 7 8 9 10 (n)
0 1 2 3 4 1 1 2 3 4 2  (кол-во бидонов)
0 1 1 1 1 5 6 1 1 1 5  (объем бидона взятого последним)
                                                        """

"""
задача о рюкзаке (куче), номер 1119 на информатиксе: 
набрать кучу весом ближайшую к W

пример: w = 8, канми 2,4,5 и 7. 

        Матрица:
     0 1 2 3 4 5 6 7 8 (w)
1  2 0 0 2 2 2 2 2 2 2
2  4 0 0 2 2 4 4 6 6 6
3  5 0 0 2 2 4 5 6 7 7
4  7 0 0 2 2 4 5 6 7 7
|i |вес камней  
T[i][w] - оптимальный вес, полученный для кучи весом w из i первый по счету камней   

w >= |вес камней  
(камень 4)
T[2][w] = T[1][w] - если брать камень
T[2][w] = 4 + T[1][w-4] - если не брать камень
                                               """
#1119
"""n, m = list(map(int, input().split()))
spi = [[0] * (m + 1) for i in range(n + 1)]
li = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j >= li[i - 1]:
            spi[i][j] = max(spi[i - 1][j], li[i - 1] + spi[i - 1][j - li[i - 1]])
        else:
            spi[i][j] = spi[i - 1][j]
print(spi[n][m])
"""

# Числа Фибоначи
"""n = int(input())
li = [1, 1]
for i in range(n - 2):
    li.append(li[-2] + li[-1])
print(li[n - 1])"""

# №203 Мячик на лесенке
"""n = int(input())
li = [0, 1, 1]
for i in range(n - 1):
    li.append(li[-3] + li[-2] + li[-1])
print(li[-1])"""


# Простая последовательность
# Условие
"""
Вычислите n-й член последовательности, заданной формулами:
a2n = an + a(n-1), 
a2n+1 = an – a(n-1),
a0 = a1 = 1."""
# Решение
"""n = int(input())
li = [1, 1]
for i in range(2, n + 1):
    if not i % 2:
        li.append(li[i // 2] + li[i // 2 - 1])
    if i % 2:
        li.append(li[(i - 1) // 2] - li[(i - 1) // 2 - 1])
print(li[-1])
"""


# Хитрая последовательность
# Условие
"""
Вычислите n-й член последовательности, заданной формулами:

a2n = an ­+ 1 (n>0), 
a2n+2 = a2n+1 - an (n>0),
a0=1, a1=1.
"""
# Решение
"""n = int(input())
li = [0] * (n + 1)
li[0] = li[1] = 1
for i in range(2, n + 1):
    if i % 2:
        li[i] = li[(i - 1) // 2 + 1] + li[(i - 1) // 2] + 1
    else:
        li[i] = li[i // 2] + 1
print(li[n])
"""


#Последовательность из 0 и 1
"""n = int(input())
li = [1, 1]
for i in range(n):
    li.append(li[-2] + li[-1])
print(li[-1])"""

#Без трех единиц
"""n = int(input())
li = [1, 1, 2]
for i in range(n - 1):
    li.append(li[-2] + li[-1] + li[-3])
print(li[-1])"""
#Взрывоопасность-2
"""n = int(input())
li = [1, 1]
for i in range(n * 2 + 2):
    li.append(li[-2] + li[-1])
for i in range(1, n * 2, 3):
    print(li[i], end=' ')
print(li)?"""

# Самый дешевый путь
n = int(input())
li = list(reversed(list(map(int, input().split()))))
cnt = n
count = 0
su = 0
i = n - 1
while i >= 0:
    if i - 1 == 0:
        su += li[i - 1]
        break
    if i == 0:
        break
    su += min(li[i], li[i - 1])
    if min(li[i], li[i - 1]) == li[i] and li[i] != li[i - 1]:
        i -= 1
    else:
        print(li[i])
        i -= 2
print(su)
