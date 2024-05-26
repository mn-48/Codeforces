for _ in range(int(input())):
    n = int(input())
    a = sorted(set(list(map(int, input().split()))))

    x = a[0]
    y = a[1] if len(a) > 1 else a[0]

    ans = "YES"
    for i in a:
        if i % x == 0 or i % y == 0:
            ans = "YES"
        else:
            ans = "NO"
            break
    print(a)
    print(ans)
