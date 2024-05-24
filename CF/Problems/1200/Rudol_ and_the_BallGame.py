for _ in range(int(input())):
    n,m,x = map(int, input().split())

    s = {x}
    for i in range(m):
        r, c = input().split()
        r = int(r)
        s = { (x+d-1) % n+1 for d in ([r], [-r], [r, -r])[int(min(c, "2"))] for x in s }
    print(len(s), *sorted(s))
