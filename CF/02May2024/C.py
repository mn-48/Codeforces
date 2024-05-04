
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [501]
    for e in a:
        b.append(b[-1]+e)
    print(*b)
        
