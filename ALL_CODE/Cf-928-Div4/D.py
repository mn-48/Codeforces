from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    c = Counter(a)
    # print(c)
    k = 2**31-1
    # print(k)

    for i in a:
        if c[i] and c[k^i]:
            n-=1
            c[i]-=1
            c[k^i]-=1
    print(n)


