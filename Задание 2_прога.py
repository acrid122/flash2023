def f(x):
    for k in range(2, int(x ** 0.5)):
        if x % k == 0:
            return False
    return True
kcount = 0
for k in range(10**5, 10**6):
    if f(k):
        k = str(k)
        if int(k[0]) % 2 == int(k[-1]) % 2 and int(k[1]) % 3 == int(k[-2]) % 3 and \
           int(k[2]) + int(k[3]) < int(k[1]) + int(k[-1]):
            count = [k.count(i) for i in k if k.count(i) == 1]
            if len(count) == 6:
                kcount+=1
print(2112 - kcount)
            
    
