for _ in range(int(input())):
    x = y =""
    for u, v in map(sorted, zip(input(), input())):
        x, y = sorted((x+v, y+u))
    print(x, y)