for _ in range(int(input())):
    p1, p2, p3 = map(int, input().split())
    print([[p1+p2, (p1+p2+p3)//2][p1+p2 > p3], -1][(p1+p2+p3) % 2])
