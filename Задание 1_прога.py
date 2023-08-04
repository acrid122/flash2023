for a in range(200):
    fl = True
    for x in range(200):
        for y in range(200):
            if ((2*x + 3*y > 30) or (x + y <= a)) == False:
                fl = False
                break
        if not fl:
            break
    if fl:
        print(a)
        break
