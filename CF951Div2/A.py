for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    y = max(a[0], a[1])
    for i in range(n-1):
        x = max(a[i], a[i+1])
        y = min(y, x)
    print(y-1)
    





























