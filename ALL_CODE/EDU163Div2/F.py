for _ in range(int(input())):
    n, q = map(int, input().split())
    for i in range(1, n):
        print(i, i+1)

    curr_distance = n-1
    u = 1
    v = 2
    for j in range(q):
        d = int(input())
        if curr_distance==d:
            print(-1, -1, -1)
        else:
            curr_distance = d
            print(u, v, n-d+1)
            v = n-d+1
