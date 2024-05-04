
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()

    p1 = 0
    p2 = 0
    cnt = 0
    while p1 < n  and p2 < m:
        if a[p1] == b[p2]:
            cnt+=1
            p1+=1
            p2+=1
        else:
            p2+=1
    print(cnt)
