for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(range(n,0, -1))
    print(*(s[:k+1][::-1]+s[k+1:]))
    