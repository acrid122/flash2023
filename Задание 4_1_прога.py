def check(x):
    k = 2
    d = 0
    mas = []
    for k in range(2, x // 2 + 1):
        if x % k == 0:
            d += 1
            mas.append(k)
        if d > 4:
            return False
        k += 1
    if d == 4:
        return mas
for k in range(234432, 234568):
    if check(k):
        print(k, check(k))
            
            
