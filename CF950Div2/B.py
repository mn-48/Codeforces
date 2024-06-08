
for _ in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))

    feb = a[f-1]
    a.sort(reverse=True)

    b = a[:k]
    a = a[k:]

    if feb in a and feb in b:
        ans = "MAYBE"

    elif feb in a:
        ans = "NO"
    else:
        ans = "YES"

    print(ans)
