li = list(map(int, input().split()))
best, summ = 0, 0
for i in range(len(li)):
    summ = max(li[i], li[i] + summ)
    best = max(best, summ)
print(best)