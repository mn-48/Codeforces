from bisect import *
T = int(input())
for _ in range(T):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.insert(0, 0)
    b.insert(0, 0)
    for i in range(q):
        d = int(input())
        p = bisect_left(a, d) - 1
        print(b[p] + (b[p + 1] - b[p]) * (d - a[p]) // (a[p + 1] - a[p]), end = ' ')
    print()