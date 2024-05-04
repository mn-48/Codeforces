from itertools import groupby

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # min group lenth will be ans of a[0]
    ans = min(len([*group]) for key, group in groupby(a) if key==a[0]) 
    print(-1 if ans==n else ans)
   